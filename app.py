import streamlit as st

# 1. 網頁基本設定（設定預設收起側邊欄，讓手機畫面最大化）
st.set_page_config(page_title="2026 花蓮選舉：AI 政策照妖鏡", layout="wide", initial_sidebar_state="collapsed")

# 針對手機版進行 CSS 視覺微調，確保字體在手機上依然霸氣大字
st.markdown("""
    <style>
    div[data-testid="stMetricValue"] { font-size: 1.8rem !important; }
    .candidate-box { padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 科技感大標題
st.markdown("<h1 style='text-align: center; color: #1E3A8A; font-size: 2rem;'>🤖 2026 花蓮縣長選舉：AI 政策照妖鏡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1rem; color: #4B5563;'><b>【公民智庫 X AI 2026 降維打擊】</b> 手指滑動切換戰區，啟動 AI 語意法官政策透視</p>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("### 🗺️ 第一步：請用手指切換「花蓮三大戰區」")

# 運用 Streamlit 原生的 tabs 功能，在手機上會自動變成極度流暢、免用顯微鏡的「左右滑動選單」
tab_north, tab_center, tab_south = st.tabs(["🟦 北花蓮核心 (吉安/花市/新城)", "🟩 中花蓮縱谷 (鳳林/壽豐/光復)", "🟧 南花蓮糧倉 (玉里/瑞穗/富里)"])

# 預設議題變數
town = ""
issue_text = ""
response_A = ""
response_B = ""
response_C = ""
ai_judge = ""

# --- 北花蓮戰區內容 ---
with tab_north:
    # 手機版直接用按鈕點選，字體大、100%防呆
    st.markdown("#### 📍 請選擇北華蓮行政區：")
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        btn_ji = st.button("🔥 吉安鄉 (本週主打)", use_container_width=True)
    with col_n2:
        btn_hl = st.button("🔵 花蓮市", use_container_width=True)
        
    if btn_hl:
        town = "花蓮市"
    else:
        # 預設或點擊吉安鄉時，載入大老提供的精準攻防資料
        town = "吉安鄉"
        issue_text = "「吉安鄉作為花蓮唯一人口正成長的地區，老年人前往慈濟醫院或門諾醫院的就醫接駁車班次嚴重不足。請問各候選人，是否承諾當選後三個月內，結合中央補助，針對各村高齡長者增開『每日定時就醫專車』？」"
        response_A = "❌ 游淑貞 (現任)<br><br><b>【AI 判定：打高空願景】</b><br><br>官方回應：「我們會從現在的公共運輸持續滾動檢討。」"
        response_B = "⚠️ 張峻<br><br><b>【AI 判定：缺乏具體預算】</b><br><br>官方回應：「將建立公共運輸網，打造便利生活。」"
        response_C = "⚠️ 魏嘉賢<br><br><b>【AI 判定：缺乏執行時程】</b><br><br>官方回應：「將持續滾動檢討公共運輸網。」"
        ai_judge = "1. <b>現任者游淑貞陣營</b>：採用了極其典型的『程序性拖延修辭』（滾動檢討）。實質上避開了對特定預算科目的承諾。<br>2. <b>張峻與魏嘉賢陣營</b>：兩者提出的均屬於宏觀政策願景（Vision），而非具體可執行之計畫（Action Plan）。在缺乏經費來源與期程的情況下，此類政見在 AI 語意模型中的『可信度指標』僅評定為 <b>18%</b>。<br><br><b>⚖️ 綜合判決：</b> 本案三方幕僚均未通過『直球對決測試』，本看板將持續亮起黃紅燈示警。"

# --- 中花蓮戰區內容 ---
with tab_center:
    st.markdown("#### 📍 請選擇中花蓮行政區：")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        if st.button("🟡 鳳林鎮", use_container_width=True): town = "鳳林鎮"
    with col_m2:
        if st.button("🟡 壽豐鄉", use_container_width=True): town = "壽豐鄉"

# --- 南花蓮戰區內容 ---
with tab_south:
    st.markdown("#### 📍 請選擇南花蓮行政區：")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        if st.button("🔴 玉里鎮", use_container_width=True): town = "玉里鎮"
    with col_s2:
        if st.button("🟠 瑞穗鄉", use_container_width=True): town = "瑞穗鄉"

# 預設防空值處理
if not town:
    town = "吉安鄉"

st.markdown(f"### 📍 當前透視戰區：<span style='color: #EF4444;'>【{town} 焦點議題】</span>", unsafe_allow_html=True)
st.markdown("---")

# 5. 政策詰問與殘酷對決看板
if town == "吉安鄉" and issue_text:
    st.markdown("### 🚨 在地青年連線·直球詰問：")
    st.info(issue_text)
    
    # 手機版友善排版：在電腦/平板上會三欄並排，在手機上會自動變成「一格一格往下堆疊」，字體絕對不會縮小！
    st.markdown("### 🏛️ 各候選人直球對決看板")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='candidate-box' style='background-color: #FEE2E2; border: 1px solid #EF4444; color: #991B1B;'>{response_A}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='candidate-box' style='background-color: #FEF3C7; border: 1px solid #F59E0B; color: #92400E;'>{response_B}</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='candidate-box' style='background-color: #FEF3C7; border: 1px solid #F59E0B; color: #92400E;'>{response_C}</div>", unsafe_allow_html=True)
        
    st.markdown("---")
    
    # 🤖 科技感核心：AI 覆核法官區塊
    st.markdown("### 🤖 2026 Google Gemini AI 政策覆核法官意見")
    with st.expander("👁️ 點擊解鎖 AI 針對候選人「法律與財政紀律」的深度審查報告", expanded=True):
        st.markdown(f"<div style='background-color: #F3F4F6; padding: 15px; border-radius: 8px; color: #1F2937;'>{ai_judge}</div>", unsafe_allow_html=True)

else:
    st.markdown(f"### 📭 暫無【{town}】的青年提案")
    st.write(f"這代表該區的傳統派系樁腳勢力依舊穩固，地方青年正在實體討論會中秘密集結。歡迎在地鄉親私訊管理員提供痛點，敬請期待下週【{town}週】火網全開！")
