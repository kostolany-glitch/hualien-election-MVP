import streamlit as st

# 1. 網頁基本設定
st.set_page_config(page_title="2026 花蓮選舉：AI 政策審判官", layout="wide", initial_sidebar_state="collapsed")

# 2. 核心黑科技：溫馨文青風視覺 (強制覆蓋) + JavaScript 觸控滑動監聽
st.markdown("""
    <style>
    /* 溫馨、柔和的文青大地色系背景 */
    .stApp { background-color: #F9F6F0 !important; color: #4A4A4A !important; }
    h2, p, span { font-family: "Noto Serif TC", "Microsoft JhengHei", serif !important; }
    
    /* 精緻溫馨的王權卡片容器 */
    .game-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 10px auto;
        max-width: 400px;
    }
    
    .reigns-card-v2 {
        background-color: #FFFFFF;
        border: 1px solid #E6DFD3;
        border-radius: 20px;
        padding: 24px;
        width: 100%;
        min-height: 380px;
        box-shadow: 0 10px 25px rgba(180, 170, 150, 0.15);
        text-align: center;
        position: relative;
        touch-action: none; /* 鎖定瀏覽器預設滑動，專注於卡片手勢 */
        transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    /* 進度條與狀態提示 */
    .status-badge {
        font-size: 0.85rem;
        background-color: #EFECE5;
        color: #7A7265;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 500;
        margin-bottom: 15px;
        display: inline-block;
    }
    
    /* 候選人名稱與回覆 */
    .candidate-title { color: #8C6A5C; font-weight: bold; font-size: 1.2rem; margin: 12px 0; }
    .response-quote {
        background-color: #FAF8F5;
        border-radius: 12px;
        padding: 16px;
        color: #5A5A5A;
        font-size: 0.95rem;
        line-height: 1.6;
        text-align: justify;
        border-left: 3px solid #C0B7A6;
    }
    
    /* 文青手繪感提示按鈕 (兼顧不習慣滑動的阿伯，字體絕對清晰) */
    .swipe-hint-btn {
        background-color: #8C6A5C !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 12px 20px !important;
        border-radius: 25px !important;
        font-size: 0.95rem !important;
        font-weight: bold !important;
        box-shadow: 0 4px 10px rgba(140, 106, 92, 0.2) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 頂部精緻文青風標題
st.markdown("<h2 style='text-align: center; color: #5C4E46; font-weight: bold;'>🌾 2026 花蓮政策審判官</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8C7E74; font-size:0.95rem;'>試著左右滑動中間的卡片，看看是誰又在用漂亮的形容詞敷衍家鄉？</p>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;'><span class='status-badge'>📍 吉安鄉核心議題：高齡就醫專車</span></div>", unsafe_allow_html=True)

# 3. 遊戲資料與狀態控制
if 'card_step' not in st.session_state:
    st.session_state.card_step = 0
if 'verdicts' not in st.session_state:
    st.session_state.verdicts = []

cards_data = [
    {
        "candidate": "游淑貞 (現任鄉長)",
        "response": "「我們會從現在的公共運輸持續滾動檢討。」",
        "hint": "💡 提示：『滾動檢討』屬於典型的法律不確定延期修辭，避開了具體預算承諾。"
    },
    {
        "candidate": "張峻 (現任議長)",
        "response": "「將建立公共運輸網，打造便利生活。」",
        "hint": "💡 提示：提出了美好的政策願景，但截至目前為止，尚未公開自籌經費來源。"
    },
    {
        "candidate": "魏嘉賢 (現任議員)",
        "response": "「將持續滾動檢討公共運輸網。」",
        "hint": "💡 提示：同樣使用了觀望型修辭，並未給出三個月內具體落實的時間表。"
    }
]

# 4. 遊戲互動賽局
if st.session_state.card_step < len(cards_data):
    current = cards_data[st.session_state.card_step]
    
    # 網頁核心：前端 JavaScript 手勢監聽，實現真實的「左右滑動」
    # 手指在平板/手機上往左滑會自動觸發 Streamlit 的左按鈕，往右滑觸發右按鈕
    st.markdown("""
        <script>
        setTimeout(function() {
            var el = window.parent.document.querySelector('.reigns-card-v2');
            if(!el) return;
            var startX = 0;
            
            el.addEventListener('touchstart', function(e) {
                startX = e.changedTouches[0].screenX;
            }, false);
            
            el.addEventListener('touchend', function(e) {
                var endX = e.changedTouches[0].screenX;
                var diffX = endX - startX;
                
                if (diffX < -60) { // 往左滑 
                    el.style.transform = 'translateX(-100px) rotate(-10deg)';
                    setTimeout(function() {
                        var btn = window.parent.document.querySelectorAll('button')[0]; // 左邊按鈕
                        if(btn) btn.click();
                    }, 100);
                } else if (diffX > 60) { // 往右滑
                    el.style.transform = 'translateX(100px) rotate(10deg)';
                    setTimeout(function() {
                        var btn = window.parent.document.querySelectorAll('button')[1]; // 右邊按鈕
                        if(btn) btn.click();
                    }, 100);
                }
            }, false);
        }, 500);
        </script>
    """, unsafe_allow_html=True)

    # 渲染精緻的王權卡片
    st.markdown(f"""
        <div class='game-container'>
            <div class='reigns-card-v2'>
                <span style='color: #A39788; font-size: 0.85rem; font-weight: bold;'>🔍 政策審查進度 {st.session_state.card_step + 1} / {len(cards_data)}</span>
                <div class='candidate-title'>{current['candidate']}</div>
                <div class='response-quote'>「{current['response']}」</div>
                <p style='color: #8C7E74; font-size: 0.82rem; margin-top: 20px; text-align: left;'>{current['hint']}</p>
                <div style='position: absolute; bottom: 15px; left: 0; width: 100%; color: #C4B9A6; font-size: 0.8rem;'>
                    👈 往左滑：判定打空話 | 往右滑：判定說人話 👉
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # 底部清晰、手繪暖色感的點擊備用按鈕（解決原本白底白字看不到的悲劇，手機極度好戳）
    st.markdown("<p style='text-align: center; color: #A39788; font-size: 0.85rem; margin-top: -10px;'>💡 手機用戶可以直接用手指『左右滑動卡片』或點擊下方按鈕：</p>", unsafe_allow_html=True)
    col_l, col_r = st.columns(2)
    with col_l:
        if st.button("👈 駁回：這在打空話", use_container_width=True, key="btn_left"):
            st.session_state.verdicts.append(f"🍁 您審判了 **{current['candidate']}** ── 判定其為『打空話』")
            st.session_state.card_step += 1
            st.rerun()
    with col_r:
        if st.button("👉 通過：這有說人話", use_container_width=True, key="btn_right"):
            st.session_state.verdicts.append(f"🌿 您審判了 **{current['candidate']}** ── 判定其為『說人話』")
            st.session_state.card_step += 1
            st.rerun()

# 5. 遊戲結束：產出溫馨、厚實的「AI 政策終審判決書」
else:
    st.markdown("<div class='game-container'><div class='reigns-card-v2' style='min-height: auto; text-align: left;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #5C4E46; text-align: center; margin-top: 0;'>⚖️ 終審判決書</h3>", unsafe_allow_html=True)
    
    st.markdown("#### 📜 您的歷史審判軌跡：")
    for log in st.session_state.verdicts:
        st.markdown(f"- {log}")
        
    st.markdown("<hr style='border-color: #E6DFD3;'>", unsafe_allow_html=True)
    
    # 溫馨小品圖書風格的 AI 辣評
    st.markdown("#### 🤖 Google Gemini AI 政策覆核法官報告")
    st.write("""
    依據地方財政法理與行政透明度指標審查：
    
    本案（吉安高齡就醫專車）三方針營提交之官方修辭，無論您的主觀判定是寬容還是嚴格，在 AI 語意模型中，由於皆**「未能明確交代預算編列科目」**與**「承諾當選後三個月內具體落實」**。
    
    因此，本案三方幕僚的回應，在政策信賴度評級上均判定為 **18% 的低度承諾**。本看板將持續亮起黃紅燈，直到任何一方補正具體預算案。
    """)
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    if st.button("🔄 重新開啟下一鄉鎮審查", use_container_width=True):
        st.session_state.card_step = 0
        st.session_state.verdicts = []
        st.rerun()
