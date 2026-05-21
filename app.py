import streamlit as st

# 1. 網頁基本設定
st.set_page_config(page_title="2026 花蓮選舉：AI 政策照妖鏡", layout="wide", initial_sidebar_state="collapsed")

# 注入戰情室暗黑風格 CSS
st.markdown("""
    <style>
    .stApp { background-color: #0D1117 !important; color: #C9D1D9 !important; }
    h1, h2, h3, p { font-family: 'Courier New', monospace, sans-serif !important; }
    
    /* 王權卡片本體風格 */
    .reigns-card {
        background: linear-gradient(145deg, #161B22, #21262D);
        border: 2px solid #30363D;
        border-radius: 16px;
        padding: 25px;
        margin: 20px auto;
        max-width: 450px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        text-align: center;
    }
    
    /* 遊戲狀態計分板 */
    .game-score {
        background-color: #090D13;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        font-size: 0.9rem;
        border: 1px solid #21262D;
    }
    </style>
""", unsafe_allow_html=True)

# 頂部遊戲化標題
st.markdown("<h2 style='text-align: center; color: #58A6FF;'>🎮 花蓮 2026：AI 政策審判官</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8B949E; font-size:0.9rem;'>【手機專用版】左右滑動（點擊）判定候選人修辭，解鎖 AI 深度辣評</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. 初始化遊戲狀態機 (Session State)
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0
if 'history' not in st.session_state:
    st.session_state.history = []

# 建立我們的「王權卡片庫」── 這次把三位候選人拆成三張獨立卡片，強迫選民一張一張「審查」
cards = [
    {
        "town": "吉安鄉 (焦點議題)",
        "issue": "👵 老人就醫接駁專車嚴重不足，是否承諾當選後三個月內結合中央補助增開？",
        "candidate": "❌ 游淑貞 (現任鄉長)",
        "response": "「我們會從現在的公共運輸持續滾動檢討。」",
        "ai_hint": "💡 AI 提示：這是程序性拖延修辭。在法理上屬於不確定概念之濫用。"
    },
    {
        "town": "吉安鄉 (焦點議題)",
        "issue": "👵 老人就醫接駁專車嚴重不足，是否承諾當選後三個月內結合中央補助增開？",
        "candidate": "⚠️ 張峻 (現任議長)",
        "response": "「將建立公共運輸網，打造便利生活。」",
        "ai_hint": "💡 AI 提示：屬於宏觀願景，但缺乏自籌款經費來源與具體規劃。"
    },
    {
        "town": "吉安鄉 (焦點議題)",
        "issue": "👵 老人就醫接駁專車嚴重不足，是否承諾當選後三個月內結合中央補助增開？",
        "candidate": "⚠️ 魏嘉賢 (現任議員)",
        "response": "「將持續滾動檢討公共運輸網。」",
        "ai_hint": "💡 AI 提示：同樣使用了『滾動檢討』，未見明確的承諾時間點。"
    }
]

# 3. 遊戲進行賽局
if st.session_state.card_index < len(cards):
    current_card = cards[st.session_state.card_index]
    
    # 頂部遊戲進度條
    st.markdown(f"""
        <div class='game-score'>
            <span style='color: #8B949E;'>當前審查進度：</span> 
            <b style='color: #58A6FF;'>{st.session_state.card_index + 1} / {len(cards)}</b>
        </div>
    """, unsafe_allow_html=True)
    
    # 呈現王權風單一卡片
    st.markdown(f"""
        <div class='reigns-card'>
            <span style='color: #F85149; font-size: 0.85rem; font-weight: bold; letter-spacing: 1px;'>📍 {current_card['town']}</span>
            <p style='font-size: 1rem; color: #C9D1D9; margin-top: 10px; line-height: 1.5;'><b>【青年詰問】</b><br>{current_card['issue']}</p>
            <hr style='border-color: #30363D;'>
            <h3 style='color: #FF7B72; margin: 10px 0;'>{current_card['candidate']}</h3>
            <div style='background-color: #0D1117; padding: 12px; border-radius: 8px; border: 1px solid #21262D; margin-bottom: 15px;'>
                <p style='color: #E6EDF2; font-size: 0.95rem; line-height: 1.5; margin: 0;'>「{current_card['response']}」</p>
            </div>
            <p style='color: #8B949E; font-size: 0.8rem; text-align: left; background-color: rgba(88,166,255,0.05); padding: 8px; border-radius: 4px;'>{current_card['ai_hint']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 王權的核心：左右滑動的抉擇按鈕（在手機畫面上超級大、極度好戳）
    col_left, col_right = st.columns(2)
    
    with col_left:
        if st.button("👈 判定：打空話 (Swipe Left)", use_container_width=True):
            st.session_state.history.append(f"🔴 你判定了 {current_card['candidate']} 為『打空話』")
            st.session_state.card_index += 1
            st.rerun()
            
    with col_right:
        if st.button("👉 判定：說人話 (Swipe Right)", use_container_width=True):
            st.session_state.history.append(f"🟢 你判定了 {current_card['candidate']} 為『說人話』")
            st.session_state.card_index += 1
            st.rerun()

# 4. 遊戲結束：產出最終的「AI 政策覆核法官判決書」
else:
    st.markdown("<h3 style='text-align: center; color: #56D364;'>⚖️ 審判完成！AI 政策法官終審報告</h3>", unsafe_allow_html=True)
    
    # 秀出玩家剛剛的判定歷史，多巴胺與參與感拉滿
    st.markdown("#### 📜 您的審判軌跡：")
    for log in st.session_state.history:
        st.write(log)
        
    st.markdown("---")
    
    # 終端機風格的 Gemini-2.5-Pro 總結報告
    st.markdown("""
        <div style='background-color: #05070B; border: 1px solid #10B981; padding: 20px; border-radius: 8px; font-family: monospace; color: #34D399; box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);'>
            <b>&gt; [SYSTEM]: 啟動 Gemini-Pro 政策終審判定...</b><br>
            <b>&gt; [VERDICT]: 綜合財政法與行政法理判定：</b><br><br>
            本案（吉安高齡就醫）三方幕僚送交之官方回應，無論您的主觀判定為何，在 AI 語意模型中，由於皆缺乏<b>「明確預算來源科目」</b>與<b>「三個月內開工期程」</b>，其『可信度指標 (Credibility Index)』均被系統強制鎖定在 <b>18%</b> 的低信賴區間。<br><br>
            <span style='color: #F87171;'>&gt; [WARN]: 警告：各陣營幕僚若欲解除黃紅燈鎖定，請速提交具體預算公文至社團管理員。</span>
        </div>
    """, unsafe_allow_html=True)
    
    # 重新挑戰按鈕
    if st.button("🔄 重新審查下一鄉鎮（清空暫存）", use_container_width=True):
        st.session_state.card_index = 0
        st.session_state.history = []
        st.rerun()
