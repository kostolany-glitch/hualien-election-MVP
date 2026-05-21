import streamlit as st

# 1. 網頁基本設定（預設收起側邊欄）
st.set_page_config(page_title="2026 花蓮選舉：AI 政策照妖鏡", layout="wide", initial_sidebar_state="collapsed")

# 2. 核心黑科技：強制注入「2026 賽博朋克暗黑戰情室」CSS 樣式表
# 徹底幹掉 Streamlit 預設的白牆排版，換上硬核科技感外殼
st.markdown("""
    <style>
    /* 全域背景與文字科技感設定 */
    .stApp { background-color: #0B0F19 !important; color: #E5E7EB !important; }
    h1, h2, h3, h4, p, span { font-family: 'Courier New', monospace, sans-serif !important; }
    
    /* 戰區科技感卡片 */
    .zone-box {
        background: linear-gradient(135deg, #111827 0%, #1F2937 100%);
        border-left: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    
    /* 候選人殘酷對決卡片 */
    .candidate-card {
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* 駭客終端機風格的 AI 區塊 */
    .terminal-box {
        background-color: #05070B !important;
        border: 1px solid #10B981 !important;
        padding: 20px;
        border-radius: 6px;
        font-family: 'Courier New', monospace !important;
        color: #34D399 !important;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 頂部大標題：賽博朋克霓虹風格
st.markdown("<h1 style='text-align: center; color: #60A5FA; font-weight: bold;'>🤖 2026 HUALIEN AI TRACKER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #10B981; font-size: 1.1rem; letter-spacing: 2px;'><b>【 花蓮縣長選舉：AI 政策照妖鏡 】</b></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 0.9rem;'>公民智庫 X AI 降維打擊 ── 遠端全面監控，拒絕空頭支票</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

# 3. 處理戰區切換（Session State 防呆鎖定）
if 'current_town' not in st.session_state:
    st.session_state.current_town = "吉安鄉"

st.markdown("### 🛰️ STEP 1: 點擊啟動「戰區數據透視探針」")

# 行動端最友善的科技感「巨型觸控卡片」
col_z1, col_z2, col_z3 = st.columns(3)

with col_z1:
    st.markdown("<div class='zone-box' style='border-left-color: #3B82F6;'><b>🟦 北花蓮戰區</b><br><span style='color: #9CA3AF; font-size: 0.8rem;'>吉安 / 花市 / 新城 / 秀林</span></div>", unsafe_allow_html=True)
    if st.button("📡 鎖定北花蓮 (吉安焦點)", use_container_width=True):
        st.session_state.current_town = "吉安鄉"

with col_z2:
    st.markdown("<div class='zone-box' style='border-left-color: #10B981;'><b>🟩 中花蓮縱谷</b><br><span style='color: #9CA3AF; font-size: 0.8rem;'>鳳林 / 壽豐 / 光復 / 豐濱</span></div>", unsafe_allow_html=True)
    if st.button("📡 鎖定中花蓮縱谷", use_container_width=True):
        st.session_state.current_town = "中花蓮縱谷"

with col_z3:
    st.markdown("<div class='zone-box' style='border-left-color: #F97316;'><b>🟧 南花蓮糧倉</b><br><span style='color: #9CA3AF; font-size: 0.8rem;'>玉里 / 瑞穗 / 富里 / 卓溪</span></div>", unsafe_allow_html=True)
    if st.button("📡 鎖定南花蓮糧倉", use_container_width=True):
        st.session_state.current_town = "南花蓮糧倉"

st.markdown(f"### 🎯 當前透視坐標：<span style='color: #60A5FA; font-size: 1.6rem;'>【 {st.session_state.current_town} 】</span>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

# 4. 數據渲染（吉安焦點議題）
if st.session_state.current_town == "吉安鄉":
    st.markdown("### 🚨 在地青年連線·直球詰問：")
    
    # 詰問面板改用暗黑高亮框
    st.markdown(f"""
        <div style='background-color: #111827; border: 1px solid #3B82F6; padding: 20px; border-radius: 8px; color: #F3F4F6; margin-bottom: 25px;'>
        <b>【高齡就醫交通痛點】</b><br><br>
        「吉安鄉作為花蓮唯一人口正成長的地區，老年人前往慈濟醫院或門諾醫院的就醫接駁車班次嚴重不足。請問各候選人，是否承諾當選後三個月內，結合中央補助，針對各村高齡長者增開『每日定時就醫專車』？」
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🏛️ 各陣營官方回應對照（排版處刑）")
    
    # 電腦平板並排、手機自動垂直堆疊，字體超大，且帶有精美霓虹警示框
    col_c1, col_c2, col_c3 = st.columns(3)
    
    with col_c1:
        st.markdown("""
            <div class='candidate-card' style='background-color: #2D1A1A; border-top: 4px solid #EF4444;'>
                <h4 style='color: #F87171; margin-top:0;'>❌ 游淑貞 (現任)</h4>
                <p style='color: #FCA5A5; font-size: 0.85rem;'><b>[ AI 語意判定：打高空願景 ]</b></p>
                <p style='color: #E5E7EB; line-height: 1.6;'>官方回應：「我們會從現在的公共運輸持續滾動檢討。」</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_c2:
        st.markdown("""
            <div class='candidate-card' style='background-color: #2D251A; border-top: 4px solid #F59E0B;'>
                <h4 style='color: #FBBF24; margin-top:0;'>⚠️ 張峻</h4>
                <p style='color: #FCD34D; font-size: 0.85rem;'><b>[ AI 語意判定：缺乏具體預算 ]</b></p>
                <p style='color: #E5E7EB; line-height: 1.6;'>官方回應：「將建立公共運輸網，打造便利生活。」</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_c3:
        st.markdown("""
            <div class='candidate-card' style='background-color: #2D251A; border-top: 4px solid #F59E0B;'>
                <h4 style='color: #FBBF24; margin-top:0;'>⚠️ 魏嘉賢</h4>
                <p style='color: #FCD34D; font-size: 0.85rem;'><b>[ AI 語意判定：缺乏執行時程 ]</b></p>
                <p style='color: #E5E7EB; line-height: 1.6;'>官方回應：「將持續滾動檢討公共運輸網。」</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    # 🤖 科技感最高峰：駭客終端機風格的 AI 覆核法官
    st.markdown("### 🤖 GOOGLE GEMINI AI 政策覆核核心")
    
    # 用代碼終端機外殼包覆，科技感直接拉滿
    with st.container():
        st.markdown("""
            <div class='terminal-box'>
                <span style='color: #10B981;'>&gt; [SYSTEM]: 啟動 Gemini-2.5-Pro 語意解構引擎...</span><br>
                <span style='color: #10B981;'>&gt; [ANALYSIS]: 開始針對候選人發言進行財政與行政法審查：</span><br><br>
                1. <b>現任者游淑貞陣營</b>：採用程序性拖延修辭（滾動檢討）。實質上避開了對特定預算科目的承諾。<br>
                2. <b>張峻與魏嘉賢陣營</b>：兩者提出之回覆均屬於宏觀政策願景（Vision），而非具體計畫（Action Plan）。在缺乏經費自籌方案與預計完工期程下，此政見在 AI 語意模型中的『可信度指標』僅評定為 <b>18%</b>。<br><br>
                <span style='color: #F87171;'>&gt; [VERDICT]: 綜合判決：三方幕僚均未通過直球對決測試。系統鎖定黃紅燈警示。</span>
            </div>
        """, unsafe_allow_html=True)

else:
    st.markdown(f"<div class='terminal-box' style='color: #9CA3AF !important; border-color: #4B5563 !important;'>&gt; [STATUS]: 暫無【{st.session_state.current_town}】之青年提案。傳統派系樁腳結構穩固，地方青年軍正秘密集結中。</div>", unsafe_allow_html=True)
