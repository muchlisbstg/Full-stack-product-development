import { useEffect, useRef, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import {
  ArrowDown, ArrowUp, Bot, Check, ChevronDown, CircleHelp, Clipboard,
  Cpu, FileText, Gauge, Github, KeyRound, LockKeyhole, MessageSquareText,
  Plus, RotateCw, SendHorizontal, Settings2, ShieldCheck, Sparkles,
  Terminal, X, Zap,
} from 'lucide-react';

const PROVIDERS = {
  openai: { label: 'OpenAI API', short: 'OpenAI', baseUrl: 'https://api.openai.com/v1', model: 'gpt-4o-mini' },
  ollama: { label: 'Ollama local', short: 'Ollama', baseUrl: 'http://localhost:11434', model: 'llama3.2' },
};
const STARTERS = [
  { icon: FileText, title: 'Shape a product idea', prompt: 'Help me turn a rough product idea into a clear one-page product brief. Ask me the most important questions first.' },
  { icon: Terminal, title: 'Build something', prompt: 'Help me plan a small full-stack app. Start by suggesting a minimal architecture and a practical first milestone.' },
  { icon: Gauge, title: 'Make a decision', prompt: 'Help me compare two options. Ask what matters most, then create a concise decision matrix.' },
  { icon: Sparkles, title: 'Write with me', prompt: 'Help me write a clear, engaging announcement. Ask for the audience, goal, and key details before drafting.' },
];

function loadPreferences() {
  try {
    return JSON.parse(localStorage.getItem('switchboard.preferences') || '{}');
  } catch {
    return {};
  }
}

function Message({ message, index }) {
  const [copied, setCopied] = useState(false);
  const isUser = message.role === 'user';
  async function copyMessage() {
    try {
      await navigator.clipboard.writeText(message.content);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1400);
    } catch {
      setCopied(false);
    }
  }
  return (
    <article className={`message-row ${isUser ? 'message-row-user' : ''}`}>
      <div className={`avatar ${isUser ? 'avatar-user' : 'avatar-assistant'}`} aria-hidden="true">
        {isUser ? <span>Y</span> : <Sparkles size={16} />}
      </div>
      <div className="message-body">
        <div className="message-meta">
          <span>{isUser ? 'You' : 'Switchboard'}</span>
          {!isUser && message.provider && <span className="meta-dot">{message.provider} · {message.model}</span>}
        </div>
        <div className={`message-content ${isUser ? 'user-content' : 'assistant-content'}`}>
          {isUser ? <p>{message.content}</p> : (
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{message.content}</ReactMarkdown>
          )}
        </div>
        {!isUser && (
          <div className="message-actions">
            {message.usage?.totalTokens && <span className="token-count">{message.usage.totalTokens.toLocaleString()} tokens</span>}
            <button className="icon-button copy-button" onClick={copyMessage} aria-label="Copy response" title="Copy response">
              {copied ? <Check size={14} /> : <Clipboard size={14} />}
              <span>{copied ? 'Copied' : 'Copy'}</span>
            </button>
          </div>
        )}
      </div>
      <span className="sr-only">Message {index + 1}</span>
    </article>
  );
}

export default function App() {
  const initial = useRef(loadPreferences()).current;
  const [provider, setProvider] = useState(initial.provider === 'ollama' ? 'ollama' : 'openai');
  const [baseUrl, setBaseUrl] = useState(initial.baseUrl || PROVIDERS[initial.provider === 'ollama' ? 'ollama' : 'openai'].baseUrl);
  const [model, setModel] = useState(initial.model || PROVIDERS[initial.provider === 'ollama' ? 'ollama' : 'openai'].model);
  const [apiKey, setApiKey] = useState('');
  const [models, setModels] = useState([]);
  const [connection, setConnection] = useState('idle');
  const [connectionMessage, setConnectionMessage] = useState('');
  const [messages, setMessages] = useState([]);
  const [draft, setDraft] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const [systemPrompt, setSystemPrompt] = useState('You are a thoughtful, capable assistant. Be clear, practical, and honest.');
  const [temperature, setTemperature] = useState(0.7);
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [scrollVisible, setScrollVisible] = useState(false);
  const bottomRef = useRef(null);
  const transcriptRef = useRef(null);
  const textareaRef = useRef(null);

  useEffect(() => {
    localStorage.setItem('switchboard.preferences', JSON.stringify({ provider, baseUrl, model }));
  }, [provider, baseUrl, model]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth', block: 'end' });
  }, [messages, busy]);

  useEffect(() => {
    const container = transcriptRef.current;
    if (!container) return undefined;
    const onScroll = () => setScrollVisible(container.scrollHeight - container.scrollTop - container.clientHeight > 160);
    container.addEventListener('scroll', onScroll, { passive: true });
    return () => container.removeEventListener('scroll', onScroll);
  }, [messages.length]);

  function switchProvider(next) {
    if (busy || next === provider) return;
    setProvider(next);
    setBaseUrl(PROVIDERS[next].baseUrl);
    setModel(PROVIDERS[next].model);
    setModels([]);
    setApiKey('');
    setConnection('idle');
    setConnectionMessage('');
    setError('');
  }

  async function testConnection() {
    if (provider === 'openai' && !apiKey.trim()) {
      setConnection('error');
      setConnectionMessage('Add your API key to connect to OpenAI.');
      return;
    }
    setConnection('checking');
    setConnectionMessage('Checking your connection…');
    try {
      const response = await fetch('/api/models', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ provider, baseUrl, apiKey }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'Could not connect to the provider.');
      setModels(data.models || []);
      setConnection('connected');
      setConnectionMessage(data.models?.length
        ? `${data.models.length} model${data.models.length === 1 ? '' : 's'} available.`
        : 'Connected. Enter a model name to continue.');
    } catch (requestError) {
      setConnection('error');
      setConnectionMessage(requestError.message || 'Could not connect. Check the URL and try again.');
    }
  }

  async function sendMessage(text = draft) {
    const content = text.trim();
    if (!content || busy || (provider === 'openai' && !apiKey.trim())) return;
    const conversation = [...messages, { role: 'user', content }];
    setMessages(conversation);
    setDraft('');
    if (textareaRef.current) textareaRef.current.style.height = '54px';
    await requestAssistant(conversation);
  }

  async function requestAssistant(conversation) {
    if (busy) return;
    setError('');
    setBusy(true);
    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({
          provider, baseUrl, apiKey, model, messages: conversation.map(({ role, content: textContent }) => ({ role, content: textContent })),
          systemPrompt, temperature,
        }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'The model request failed.');
      setMessages([...conversation, { role: 'assistant', content: data.text, provider: PROVIDERS[provider].short, model, usage: data.usage }]);
      setConnection('connected');
    } catch (requestError) {
      setError(requestError.message || 'Something went wrong. Please try again.');
    } finally {
      setBusy(false);
      textareaRef.current?.focus();
    }
  }

  function submit(event) {
    event.preventDefault();
    sendMessage();
  }

  function onDraftChange(event) {
    setDraft(event.target.value);
    event.target.style.height = '54px';
    event.target.style.height = `${Math.min(event.target.scrollHeight, 180)}px`;
  }

  function startFresh() {
    if (busy) return;
    setMessages([]);
    setDraft('');
    setError('');
    setSidebarOpen(false);
    textareaRef.current?.focus();
  }

  const isReady = provider === 'ollama' || Boolean(apiKey.trim());

  return (
    <div className="app-shell">
      <aside className={`sidebar ${sidebarOpen ? 'sidebar-open' : ''}`}>
        <div className="brand-lockup">
          <div className="brand-mark"><Zap size={18} fill="currentColor" strokeWidth={2.3} /></div>
          <span>switchboard</span>
          <span className="brand-beta">LOCAL</span>
        </div>
        <button className="new-chat-button" onClick={startFresh}><Plus size={17} /> <span>New conversation</span><kbd>⌘ K</kbd></button>
        <div className="sidebar-section-label">WORKSPACE</div>
        <button className="side-link active"><MessageSquareText size={17} /><span>Chat</span></button>
        <button className="side-link" onClick={() => setSettingsOpen(true)}><Settings2 size={17} /><span>Agent settings</span></button>
        <div className="sidebar-divider" />
        <div className="history-heading"><span className="sidebar-section-label">RECENT</span><button className="quiet-icon" aria-label="Recent conversations"><ChevronDown size={15} /></button></div>
        {messages.length > 0 ? (
          <button className="history-item" onClick={() => setSidebarOpen(false)}><span className="history-mark" /><span>{messages.find((message) => message.role === 'user')?.content || 'New conversation'}</span></button>
        ) : (
          <div className="history-empty"><div className="history-empty-icon"><MessageSquareText size={16} /></div><p>Your conversations<br />will show up here.</p></div>
        )}
        <div className="sidebar-spacer" />
        <div className="privacy-note"><div className="privacy-icon"><ShieldCheck size={15} /></div><div><strong>Your workspace, your rules</strong><span>Keys stay in this session.</span></div></div>
        <a className="sidebar-footer-link" href="https://github.com/muchlisbstg/Full-stack-product-development" target="_blank" rel="noreferrer"><Github size={15} /> Project repository <ArrowUp size={13} className="external-arrow" /></a>
      </aside>

      {sidebarOpen && <button className="sidebar-scrim" aria-label="Close menu" onClick={() => setSidebarOpen(false)} />}

      <main className="main-panel">
        <header className="topbar">
          <div className="topbar-left"><button className="mobile-menu" onClick={() => setSidebarOpen((open) => !open)} aria-label="Toggle navigation"><MessageSquareText size={18} /></button><span className="breadcrumb-muted">Workspace</span><span className="breadcrumb-slash">/</span><span className="breadcrumb-current">Chat</span></div>
          <div className="topbar-actions"><span className="local-badge"><span className="local-dot" /> PRIVATE SESSION</span><button className="help-button" title="Open agent settings" onClick={() => setSettingsOpen(true)}><CircleHelp size={17} /><span>Help</span></button><button className="settings-button" onClick={() => setSettingsOpen(true)} aria-label="Open agent settings"><Settings2 size={17} /></button></div>
        </header>

        <div className="workspace-layout">
          <section className="conversation-column">
            <div className={`transcript ${messages.length ? 'transcript-active' : ''}`} ref={transcriptRef}>
              {messages.length === 0 ? (
                <div className="welcome-screen">
                  <div className="welcome-eyebrow"><span className="eyebrow-line" /> YOUR AI WORKSPACE <span className="eyebrow-line" /></div>
                  <div className="welcome-orbit"><div className="orbit-ring orbit-ring-one" /><div className="orbit-ring orbit-ring-two" /><div className="orbit-glow" /><div className="orbit-core"><Sparkles size={28} strokeWidth={1.7} /></div><span className="orbit-node orbit-node-one"><Bot size={15} /></span><span className="orbit-node orbit-node-two"><Cpu size={15} /></span></div>
                  <h1>One workspace.<br /><span>Two kinds of intelligence.</span></h1>
                  <p className="welcome-subtitle">Pick the model that fits the moment. Keep your context, your flow, and your options open.</p>
                  <div className="starter-grid">
                    {STARTERS.map(({ icon: Icon, title, prompt }) => <button className="starter-card" key={title} onClick={() => { setDraft(prompt); textareaRef.current?.focus(); }}><span className="starter-icon"><Icon size={17} /></span><span className="starter-title">{title}</span><ArrowUp size={14} className="starter-arrow" /></button>)}
                  </div>
                  <div className="welcome-footnote"><LockKeyhole size={13} /> Your OpenAI key stays in memory. Ollama runs on your machine.</div>
                </div>
              ) : (
                <div className="messages-list">
                  {messages.map((message, index) => <Message key={`${index}-${message.role}`} message={message} index={index} />)}
                  {busy && <div className="message-row"><div className="avatar avatar-assistant"><Sparkles size={16} /></div><div className="message-body"><div className="message-meta"><span>Switchboard</span><span className="meta-dot">Thinking with {PROVIDERS[provider].short}</span></div><div className="typing-indicator"><span /><span /><span /></div></div></div>}
                  {error && <div className="error-banner"><span className="error-symbol">!</span><span>{error}</span><button onClick={() => requestAssistant(messages)}>Try again</button></div>}
                  <div ref={bottomRef} />
                </div>
              )}
            </div>
            {scrollVisible && <button className="scroll-latest" onClick={() => bottomRef.current?.scrollIntoView({ behavior: 'smooth' })}><ArrowDown size={15} /> Latest</button>}

            <div className="composer-wrap">
              <form className="composer" onSubmit={submit}>
                <textarea ref={textareaRef} value={draft} onChange={onDraftChange} onKeyDown={(event) => { if (event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); submit(event); } }} placeholder={provider === 'openai' && !apiKey ? 'Add your OpenAI key to start chatting…' : 'Message your agent…'} rows={1} aria-label="Message your agent" />
                <div className="composer-bottom"><div className="composer-hint"><span><kbd>↵</kbd> to send</span><span className="hint-divider">·</span><span><kbd>⇧ ↵</kbd> for a new line</span></div><button className="send-button" type="submit" disabled={!draft.trim() || busy || !isReady} aria-label="Send message">{busy ? <span className="send-spinner" /> : <SendHorizontal size={17} />}</button></div>
              </form>
              <div className="composer-caption">AI can make mistakes. Check important information.</div>
            </div>
          </section>

          <aside className="control-column">
            <div className="control-panel">
              <div className="panel-heading"><div><span className="panel-kicker">YOUR AGENT</span><h2>Model setup</h2></div><div className="panel-heading-icon"><Settings2 size={17} /></div></div>
              <p className="panel-description">Choose a provider and model for this conversation.</p>
              <div className="provider-toggle" role="tablist" aria-label="AI provider">
                <button className={provider === 'openai' ? 'provider-tab selected' : 'provider-tab'} role="tab" aria-selected={provider === 'openai'} onClick={() => switchProvider('openai')} disabled={busy}><span className="provider-symbol openai-symbol"><Sparkles size={15} /></span>OpenAI</button>
                <button className={provider === 'ollama' ? 'provider-tab selected' : 'provider-tab'} role="tab" aria-selected={provider === 'ollama'} onClick={() => switchProvider('ollama')} disabled={busy}><span className="provider-symbol ollama-symbol"><Cpu size={15} /></span>Ollama</button>
              </div>
              <div className="field-group">
                <div className="field-label-row"><label htmlFor="model">MODEL</label><button className="field-action" onClick={testConnection} disabled={connection === 'checking'} title="Load available models">{connection === 'checking' ? <span className="tiny-spinner" /> : <RotateCw size={13} />}<span>{connection === 'checking' ? 'Checking' : 'Load models'}</span></button></div>
                <input id="model" className="text-field model-field" list="available-models" value={model} onChange={(event) => setModel(event.target.value)} placeholder="e.g. llama3.2" disabled={busy} />
                <datalist id="available-models">{models.map((name) => <option key={name} value={name} />)}</datalist>
              </div>
              {provider === 'openai' && <div className="field-group"><div className="field-label-row"><label htmlFor="api-key">API KEY</label><span className="field-safe"><LockKeyhole size={11} /> SESSION ONLY</span></div><div className="input-with-icon"><KeyRound size={15} /><input id="api-key" type="password" autoComplete="off" className="text-field" value={apiKey} onChange={(event) => { setApiKey(event.target.value); setConnection('idle'); setConnectionMessage(''); }} placeholder="sk-••••••••••••••••" disabled={busy} /></div></div>}
              <div className="field-group"><div className="field-label-row"><label htmlFor="endpoint">{provider === 'openai' ? 'API BASE URL' : 'OLLAMA SERVER'}</label></div><input id="endpoint" className="text-field endpoint-field" value={baseUrl} onChange={(event) => { setBaseUrl(event.target.value); setConnection('idle'); setConnectionMessage(''); }} placeholder={PROVIDERS[provider].baseUrl} disabled={busy} /></div>
              <div className={`connection-status status-${connection}`}><span className="status-indicator">{connection === 'checking' ? <span className="tiny-spinner" /> : connection === 'connected' ? <Check size={12} /> : connection === 'error' ? <X size={11} /> : <span />}</span><span>{connectionMessage || (provider === 'ollama' ? 'Ready when Ollama is running.' : 'API key required to connect.')}</span></div>
              <button className="test-button" onClick={testConnection} disabled={connection === 'checking'}>{connection === 'checking' ? 'Connecting…' : 'Test connection'}<ArrowUp size={14} className="test-button-arrow" /></button>
              <div className="panel-divider" />
              <button className="advanced-row" onClick={() => setSettingsOpen(true)}><span className="advanced-icon"><Gauge size={15} /></span><span><strong>Agent behavior</strong><small>Instructions &amp; temperature</small></span><ArrowUp size={14} className="advanced-arrow" /></button>
            </div>
            <div className="provider-tip"><div className="tip-top"><span className="tip-mark"><Zap size={13} fill="currentColor" /></span><span>QUICK TIP</span></div><p>{provider === 'ollama' ? <>New to local models? Try <code>ollama pull llama3.2</code> in your terminal first.</> : <>Keys are kept in this page's memory only — never saved to your browser storage.</>}</p><a href="https://github.com/muchlisbstg/Full-stack-product-development#start-the-app" target="_blank" rel="noreferrer">Read the setup guide <ArrowUp size={12} /></a></div>
            <div className="panel-footnote"><ShieldCheck size={14} /> <span>Private by design<br /><small>Requests go through your local API.</small></span></div>
          </aside>
        </div>
      </main>

      {settingsOpen && <div className="modal-scrim" onClick={() => setSettingsOpen(false)}><section className="settings-modal" role="dialog" aria-modal="true" aria-labelledby="settings-title" onClick={(event) => event.stopPropagation()}><div className="modal-heading"><div className="modal-heading-icon"><Settings2 size={18} /></div><div><span className="panel-kicker">CUSTOMIZE</span><h2 id="settings-title">Agent behavior</h2></div><button className="modal-close" onClick={() => setSettingsOpen(false)} aria-label="Close settings"><X size={18} /></button></div><p className="modal-description">Set the role and response style for this conversation. These settings stay in memory and aren't saved.</p><label className="modal-label" htmlFor="system-prompt">SYSTEM INSTRUCTIONS</label><textarea id="system-prompt" className="system-prompt-field" value={systemPrompt} onChange={(event) => setSystemPrompt(event.target.value)} rows={5} placeholder="Describe how your assistant should behave…" /><div className="temperature-header"><div><label className="modal-label" htmlFor="temperature">CREATIVITY</label><p>Lower is focused. Higher is more varied.</p></div><span className="temperature-value">{Number(temperature).toFixed(1)}</span></div><input id="temperature" className="temperature-slider" type="range" min="0" max="2" step="0.1" value={temperature} onChange={(event) => setTemperature(Number(event.target.value))} /><div className="slider-labels"><span>Precise</span><span>Balanced</span><span>Creative</span></div><div className="modal-actions"><span><LockKeyhole size={13} /> Session only</span><button onClick={() => setSettingsOpen(false)}>Done <Check size={14} /></button></div></section></div>}
    </div>
  );
}
