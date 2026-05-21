import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁基本設定
st.set_page_config(page_title="2026 花蓮選舉：AI 政策審判官", layout="wide", initial_sidebar_state="collapsed")

# 2. 定義文青風 HTML 卡片模板
html_template = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;600;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg: #F5F0E8; --card-bg: #FFFDF9; --card-border: #E8DFD0;
    --text-primary: #2C2416; --text-secondary: #7A6E62; --text-muted: #A89E94;
    --accent-red: #C0392B; --accent-green: #27714A; --accent-amber: #9A6A1A;
    --stamp-red: rgba(192, 57, 43, 0.12); --stamp-green: rgba(39, 113, 74, 0.12); --ink-line: #D4C9B8;
  }
  body {
    font-family: 'Noto Sans TC', sans-serif; background-color: var(--bg);
    background-image: repeating-linear-gradient(0deg, transparent, transparent 28px, rgba(180,168,148,0.08) 28px, rgba(180,168,148,0.08) 29px);
    padding: 10px 4px; color: var(--text-primary); overflow: hidden;
  }
  .progress-row { display: flex; align-items: center; gap: 10px; width: 100%; max-width: 340px; margin: 0 auto 20px; }
  .progress-bar-track { flex: 1; height: 3px; background: var(--ink-line); border-radius: 2px; overflow: hidden; }
  .progress-bar-fill { height: 100%; background: var(--text-secondary); border-radius: 2px; transition: width 0.3s; }
  .progress-label { font-size: 12px; color: var(--text-muted); white-space: nowrap; }
  .deck { position: relative; width: 100%; max-width: 340px; height: 410px; margin: 0 auto 20px; touch-action: none; }
  .shadow-card { position: absolute; width: 100%; border-radius: 20px; background: var(--card-bg); border: 1px solid var(--card-border); }
  .shadow-card-2 { height: 380px; top: 16px; left: 8px; right: 8px; width: auto; opacity: 0.5; }
  .shadow-card-1 { height: 390px; top: 8px; left: 4px; right: 4px; width: auto; opacity: 0.75; }
  .main-card {
    position: absolute; top: 0; left: 0; width: 100%; height: 400px; border-radius: 20px; background: var(--card-bg);
    border: 1px solid var(--card-border); padding: 24px 20px; cursor: grab; user-select: none; will-change: transform;
    box-shadow: 0 4px 20px rgba(100, 80, 50, 0.08); display: flex; flex-direction: column;
  }
  .main-card:active { cursor: grabbing; }
  .card-number { font-size: 11px; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 12px; text-align: center; }
  .candidate-name { font-family: 'Noto Serif TC', serif; font-size: 20px; font-weight: 700; color: var(--text-primary); text-align: center; margin-bottom: 4px; }
  .candidate-role { font-size: 12px; color: var(--text-muted); text-align: center; margin-bottom: 16px; }
  .divider { width: 40px; height: 1px; background: var(--ink-line); margin: 0 auto 16px; }
  .quote-block { background: #FAF7F2; border-left: 3px solid var(--ink-line); border-radius: 0 10px 10px 0; padding: 12px 14px; font-size: 14px; line-height: 1.6; color: var(--text-primary); font-family: 'Noto Serif TC', serif; margin-bottom: 12px; }
  .hint-text { font-size: 12px; color: var(--text-secondary); line-height: 1.5; flex: 1; }
  .hint-text strong { color: var(--accent-amber); }
  .swipe-hint { display: flex; justify-content: space-between; align-items: center; margin-top: auto; padding-top: 12px; border-top: 1px solid var(--ink-line); }
  .swipe-label { font-size: 11px; color: var(--text-muted); }
  .verdict-overlay { position: absolute; inset: 0; border-radius: 20px; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.1s; }
  .verdict-overlay.reject { background: var(--stamp-red); }
  .verdict-overlay.pass { background: var(--stamp-green); }
  .verdict-stamp { font-family: 'Noto Serif TC', serif; font-size: 34px; font-weight: 700; padding: 8px 16px; border-radius: 8px; border: 3px solid; letter-spacing: 0.08em; transform: rotate(-12deg); opacity: 0; }
  .verdict-overlay.reject .verdict-stamp { color: var(--accent-red); border-color: var(--accent-red); }
  .verdict-overlay.pass .verdict-stamp { color: var(--accent-green); border-color: var(--accent-green); transform: rotate(8deg); }
  .btn-row { display: flex; gap: 12px; width: 100%; max-width: 340px; margin: 0 auto; }
  .verdict-btn { flex: 1; padding: 12px 10px; border-radius: 14px; border: 1.5px solid; background: transparent; font-size: 13px; font-weight: 500; cursor: pointer; transition: background 0.15s; line-height: 1.3; text-align: center; }
  .btn-reject { color: var(--accent-red); border-color: rgba(192, 57, 43, 0.35); }
  .btn-pass { color: var(--accent-green); border-color: rgba(39, 113, 74, 0.35); }
  .result-screen { display: none; flex-direction: column; align-items: center; width: 100%; max-width: 340px; margin: 0 auto; }
  .result-screen.active { display: flex; }
  .result-card { width: 100%; background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 20px; padding: 24px 20px; margin-bottom: 16px; }
  .result-title { font-family: 'Noto Serif TC', serif; font-size: 18px; font-weight: 700; text-align: center; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--ink-line); }
  .verdict-log-item { display: flex; align-items: center; gap: 12px; padding: 8px 0; border-bottom: 1px dashed var(--ink-line); font-size: 14px; }
  .verdict-tag { font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px; }
  .tag-reject { background: rgba(192,57,43,0.1); color: var(--accent-red); }
  .tag-pass { background: rgba(39,113,74,0.1); color: var(--accent-green); }
  .ai-report { background: #F7F4EE; border-radius: 12px; padding: 16px; margin-top: 12px; }
  .ai-report-header { font-size: 12px; color: var(--text-muted); margin-bottom: 8px; }
  .ai-report p { font-size: 13px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 8px; }
  .credibility-row { display: flex; align-items: center; gap: 10px; margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--ink-line); }
  .credibility-track { flex: 1; height: 4px; background: var(--ink-line); border-radius: 2px; overflow: hidden; }
  .credibility-fill { height: 100%; width: 18%; background: var(--accent-red); }
  .credibility-value { font-size: 13px; font-weight: 700; color: var(--accent-red); }
  .restart-btn { width: 100%; padding: 12px; border-radius: 14px; border: 1.5px solid var(--card-border); background: var(--card-bg); font-size: 13px; color: var(--text-secondary); cursor: pointer; }
  @keyframes flyLeft { to { transform: translateX(-130%) rotate(-25deg); opacity: 0; } }
  @keyframes flyRight { to { transform: translateX(130%) rotate(25deg); opacity: 0; } }
  .fly-left { animation: flyLeft 0.35s ease forwards; }
  .fly-right { animation: flyRight 0.35s ease forwards; }
</style>
</head>
<body>

<div class="progress-row" id="progressRow">
  <div class="progress-bar-track"><div class="progress-bar-fill" id="progressFill" style="width: 0%"></div></div>
  <div class="progress-label" id="progressLabel">0 / 3</div>
</div>

<div id="gameArea">
  <div class="deck" id="deck">
    <div class="shadow-card shadow-card-2"></div>
    <div class="shadow-card shadow-card-1"></div>
    <div class="main-card" id="mainCard">
      <div class="verdict-overlay reject" id="overlayReject"><div class="verdict-stamp">打空話</div></div>
      <div class="verdict-overlay pass" id="overlayPass"><div class="verdict-stamp">說人話</div></div>
      <div class="card-number" id="cardNumber">第 1 張 · 共 3 張</div>
      <div class="candidate-name" id="candidateName"></div>
      <div class="candidate-role" id="candidateRole"></div>
      <div class="divider"></div>
      <div class="quote-block" id="quoteText"></div>
      <div class="hint-text" id="hintText"></div>
      <div class="swipe-hint">
        <span class="swipe-label">← 打空話</span>
        <span style="font-size:11px; color: var(--text-muted)">指尖左右滑動卡片</span>
        <span class="swipe-label">說人話 →</span>
      </div>
    </div>
  </div>
  <div class="btn-row">
    <button class="verdict-btn btn-reject" id="btnReject" onclick="doVerdict('reject')">← 駁回<br><span style="font-size:10px; font-weight:400; opacity:0.8">這在打空話</span></button>
    <button class="verdict-btn btn-pass" id="btnPass" onclick="doVerdict('pass')">通過 →<br><span style="font-size:10px; font-weight:400; opacity:0.8">這有說人話</span></button>
  </div>
</div>

<div class="result-screen" id="resultScreen">
  <div class="result-card">
    <div class="result-title">⚖️ 終審判決書</div>
    <div id="verdictLog"></div>
    <div class="ai-report">
      <div class="ai-report-header">🤖 GEMINI AI 政策覆核報告</div>
      <p>__AI_REPORT_1__</p>
      <p>__AI_REPORT_2__</p>
      <div class="credibility-row">
        <span class="credibility-label">政策信賴度評級</span>
        <div class="credibility-track"><div class="credibility-fill"></div></div>
        <span class="credibility-value">18%</span>
      </div>
    </div>
  </div>
  <button class="restart-btn" onclick="restart()">🔄 重新開啟審查</button>
</div>

<script>
const cards = [
  { name: "游淑貞", role: "現任吉安鄉長", quote: "「我們會從現在的公共運輸持續滾動檢討。」", hint: "「<strong>滾動檢討</strong>」是典型的程序性延期修辭，在行政法學上屬於不確定法律概念的運用，實質上避開了特定預算科目的承諾。" },
  { name: "張峻", role: "現任花蓮縣議長", quote: "「將建立公共運輸網，打造便利生活。」", hint: "提出了美好的<strong>政策願景（Vision）</strong>，但截至目前尚未公開任何自籌經費來源，也缺乏具體完工期程。" },
  { name: "魏嘉賢", role: "現任花蓮縣議員", quote: "「將持續滾動檢討公共運輸網。」", hint: "同樣使用了<strong>觀望型修辭</strong>，並未給出三個月內具體落實的時間表，亦無配套預算說明。" }
];

let current = 0; let verdicts = []; let isDragging = false; let startX = 0; let currentX = 0;

function loadCard() {
  if (current >= cards.length) { showResult(); return; }
  const c = cards[current]; const card = document.getElementById('mainCard');
  card.style.transform = ''; card.classList.remove('fly-left', 'fly-right');
  document.getElementById('cardNumber').textContent = `第 ${current + 1} 張 · 共 ${cards.length} 張`;
  document.getElementById('candidateName').textContent = c.name;
  document.getElementById('candidateRole').textContent = c.role;
  document.getElementById('quoteText').textContent = c.quote;
  document.getElementById('hintText').innerHTML = c.hint;
  document.getElementById('overlayReject').style.opacity = 0;
  document.getElementById('overlayPass').style.opacity = 0;
  document.getElementById('progressFill').style.width = (current / cards.length) * 100 + '%';
  document.getElementById('progressLabel').textContent = `${current} / ${cards.length}`;
}

function doVerdict(type) {
  const card = document.getElementById('mainCard');
  document.getElementById('overlayReject').style.opacity = type==='reject'?1:0;
  document.getElementById('overlayPass').style.opacity = type==='pass'?1:0;
  document.getElementById('overlayReject').querySelector('.verdict-stamp').style.opacity = type==='reject'?1:0;
  document.getElementById('overlayPass').querySelector('.verdict-stamp').style.opacity = type==='pass'?1:0;
  setTimeout(() => {
    card.classList.add(type === 'reject' ? 'fly-left' : 'fly-right');
    verdicts.push({ name: cards[current].name, type });
    setTimeout(() => { current++; loadCard(); }, 350);
  }, 200);
}

const card = document.getElementById('mainCard');
function onStart(x) { isDragging = true; startX = x; currentX = 0; card.style.transition = 'none'; }
function onMove(x) {
  if (!isDragging) return; currentX = x - startX;
  card.style.transform = `translateX(${currentX}px) rotate(${currentX * 0.05}deg)`;
  const threshold = 40;
  if (currentX < -threshold) {
    document.getElementById('overlayReject').style.opacity = Math.min(1, (Math.abs(currentX)-threshold)/60);
    document.getElementById('overlayReject').querySelector('.verdict-stamp').style.opacity = 1;
  } else if (currentX > threshold) {
    document.getElementById('overlayPass').style.opacity = Math.min(1, (currentX-threshold)/60);
    document.getElementById('overlayPass').querySelector('.verdict-stamp').style.opacity = 1;
  } else {
    document.getElementById('overlayReject').style.opacity = 0; document.getElementById('overlayPass').style.opacity = 0;
  }
}
function onEnd() {
  if (!isDragging) return; isDragging = false; card.style.transition = 'transform 0.2s';
  if (currentX < -70) doVerdict('reject'); else if (currentX > 70) doVerdict('pass'); else card.style.transform = '';
}
card.addEventListener('touchstart', e => onStart(e.touches[0].clientX), { passive: true });
card.addEventListener('touchmove', e => { e.preventDefault(); onMove(e.touches[0].clientX); }, { passive: false });
card.addEventListener('touchend', onEnd);
card.addEventListener('mousedown', e => onStart(e.clientX));
document.addEventListener('mousemove', e => onMove(e.clientX));
document.addEventListener('mouseup', onEnd);

function showResult() {
  document.getElementById('gameArea').style.display = 'none'; document.getElementById('progressRow').style.display = 'none';
  document.getElementById('resultScreen').classList.add('active');
  document.getElementById('verdictLog').innerHTML = verdicts.map(v => `
    <div class="verdict-log-item">
      <span class="verdict-tag ${v.type === 'reject' ? 'tag-reject' : 'tag-pass'}">${v.type === 'reject' ? '打空話' : '說人話'}</span>
      <strong>${v.name}</strong> 的政見回覆
    </div>
  `).join('');
}
function restart() { current = 0; verdicts = []; document.getElementById('resultScreen').classList.remove('active'); document.getElementById('gameArea').style.display = ''; document.getElementById('progressRow').style.display = ''; loadCard(); }
loadCard();
</script>
</body>
</html>
"""

# 3. 在 Python 裡精準控管法官辣評文字
# 【防呆裝甲】：全面改用三重引號 """，徹底防禦平板複製貼上產生的「隱藏換行」錯誤
ai_p1 = """本案（吉安高齡就醫專車）三方針營提交之官方修辭，經語意結構解構，皆未能明確交代預算編列科目，亦未承諾當選後三個月內具體落實之時程表。"""

ai_p2 = """在法律與財政紀律分析中，「滾動檢討」與「打造便利生活」屬於典型的程序性拖延修辭，因此在 AI 模型中其『政策信賴度評級』被判定為 18% 的低度承諾區間。本看板將維持警示燈號，引導在地鄉親持續施壓。"""

# 安全替換
final_html = html_template.replace("__AI_REPORT_1__", ai_p1).replace("__AI_REPORT_2__", ai_p2)

# 4. 網頁外殼大標題 (同樣套上防彈三重引號)
st.markdown("""<h2 style='text-align: center; color: #2C2416; font-family: serif; font-weight: 700; margin-top:20px;'>🌾 2026 花蓮縣長選舉：政策照妖鏡</h2>""", unsafe_allow_html=True)
st.markdown("""<p style='text-align: center; color: #7A6E62; font-size: 0.9rem;'>由外地遊子與地方青年智庫獨立發起 ── 公民科技 X AI 降維打擊</p>""", unsafe_allow_html=True)
st.markdown("""<p style='text-align: center; color: #A89E94; font-size: 0.85rem; margin-top: -10px;'>📍 本週焦點戰區：【吉安鄉 · 高齡就醫接駁車專案】</p>""", unsafe_allow_html=True)

# 5. 一鍵渲染完全體卡片遊戲
components.html(final_html, height=530, scrolling=False)
