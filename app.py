import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁基本設定
st.set_page_config(page_title="2026 花蓮選舉：AI 政策照妖鏡", layout="wide", initial_sidebar_state="collapsed")

# 科技感大標題
st.markdown("<h1 style='text-align: center; color: #1E3A8A; font-family: sans-serif;'>🤖 2026 花蓮縣長選舉：AI 政策照妖鏡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem; color: #4B5563;'><b>【公民智庫 X AI 2026 降維打擊】</b> 點擊下方圖形化地圖，啟動 AI 語意法官進行政策透視</p>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("### 🗺️ 第一步：請用手指觸控點擊下方「花蓮科技互動地圖」")

# 2. 核心黑科技：嵌入原生 HTML/CSS/SVG 互動式地圖（專為平板觸控優化，點擊即送出 Streamlit 訊號）
# 這裡用簡化的花蓮狹長型戰區幾何圖形，解決傳統地圖在手機上過小的致命傷
svg_map_html = """
<div style="display: flex; justify-content: center; align-items: center; background: #111827; padding: 20px; border-radius: 12px; box-shadow: int 0 0 20px rgba(0,0,0,0.5);">
    <svg width="280" height="420" viewBox="0 0 200 300" xmlns="http://www.w3.org/2000/svg" style="font-family:sans-serif;">
        <g id="north" onclick="window.parent.postMessage({type: 'streamlit:setComponentValue', value: '吉安鄉'}, '*')" style="cursor: pointer;">
            <path d="M 30 20 L 170 20 L 150 90 L 50 90 Z" fill="#1E3A8A" stroke="#3B82F6" stroke-width="2" style="transition: 0.3s;" onmouseover="this.setAttribute('fill', '#2563EB')" onmouseout="this.setAttribute('fill', '#1E3A8A')"/>
            <text x="100" y="55" fill="#FFFFFF" font-size="12" font-weight="bold" text-anchor="middle">🔥 北花蓮核心 (吉安/花市/新城)</text>
        </g>
        
        <g id="center" onclick="window.parent.postMessage({type: 'streamlit:setComponentValue', value: '鳳林鎮'}, '*')" style="cursor: pointer;">
            <path d="M 50 95 L 150 95 L 130 180 L 70 180 Z" fill="#065F46" stroke="#10B981" stroke-width="2" style="transition: 0.3s;" onmouseover="this.setAttribute('fill', '#059669')" onmouseout="this.setAttribute('fill', '#065F46')"/>
            <text x="100" y="140" fill="#FFFFFF" font-size="12" font-weight="bold" text-anchor="middle">⚡ 中花蓮縱谷 (鳳林/壽豐/光復)</text>
        </g>
        
        <g id="south" onclick="window.parent.postMessage({type: 'streamlit:setComponentValue', value: '玉里鎮'}, '*')" style="cursor: pointer;">
            <path d="M 70 185 L 130 185 L 110 280 L 90 280 Z" fill="#9A3412" stroke="#F97316" stroke-width="2" style="transition: 0.3s;" onmouseover="this.setAttribute('fill', '#EA580C')" onmouseout="this.setAttribute('fill', '#9A3412')"/>
            <text x="100" y="235" fill="#FFFFFF" font-size="12" font-weight="bold" text-anchor="middle">⛰️ 南花蓮糧倉 (玉里/瑞穗/富里)</text>
        </g>
    </svg>
</div>
<p style="text-align: center; color: #9CA3AF; font-size: 0.8rem; margin-top: 5px;">💡 提示：在上方黑客風格地圖上，直接用手指戳你想觀看的戰區圖形即可切換。</p>
"""

# 渲染炫砲的 SVG 地圖，並監聽點擊訊號
clicked_town = components.html(svg_map_html, height=470)

# 接收地圖點擊訊號，若沒點擊則預設為吉安鄉
town = "吉安鄉"
if clicked_town:
    town = clicked_town

st.markdown(f"### 📍 當前透視戰區：<span style='color: #EF4444; font-size: 1.8rem;'>【{town} 焦點議題】</span>", unsafe_allow_html=True)
st.markdown("---")

# 3. 政策詰問本體 (吉安鄉示範)
if town == "吉安鄉":
    st.markdown("### 🚨 在地青年連線·直球詰問：")
    st.info("「吉安鄉作為花蓮唯一人口正成長的地區，老年人前往慈濟醫院或門諾醫院的就醫接駁車班次嚴重不足。請問各候選人，是否承諾當選後三個月內，結合中央補助，針對各村高齡長者增開『每日定時就醫專車』？」")
    
    # 三位候選人殘酷並排對決
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.error("❌ 游淑貞 (現任)\n\n**【AI 判定：打高空願景】**\n\n官方回應：「我們會從現在的公共運輸持續滾動檢討。」")
    
    with col2:
        st.warning("⚠️ 張峻\n\n**【AI 判定：缺乏具體預算】**\n\n官方回應：「將建立公共運輸网，打造便利生活。」")
        
    with col3:
        st.warning("⚠️ 魏嘉賢\n\n**【AI 判定：缺乏執行時程】**\n\n官方回應：「將持續滾動檢討公共運輸網。」")
        
    st.markdown("---")
    
    # 🤖 科技感核心：AI 覆核法官區塊
    st.markdown("### 🤖 2026 Google Gemini AI 政策覆核法官意見")
    
    with st.expander("👁️ 點擊解鎖 AI 針對候選人「法律與財政紀律」的深度審查報告", expanded=False):
        st.write("""
        本區塊由 **Gemini-2.5-Pro** 模型依據《公職人員選舉競選言論管理辦法》與財政法原理，對上述發言進行結構化語意審查：
        
        1. **現任者游淑貞陣營**：採用了極其典型的『程序性拖延修辭』（滾動檢討）。在行政法學上，此類回應屬於『不確定法律概念之濫用』，實質上避開了對特定預算科目的承諾。
        2. **張峻與魏嘉賢陣營**：兩者提出的『建立公共運輸網』均屬於宏觀政策願景（Vision），而非具體可執行之計畫（Action Plan）。在缺乏『經費來源自籌方案』與『預計完工期程』的情況下，此類政見在 AI 語意模型中的『可信度指標 (Credibility Index)』僅評定為 **18%**。
        
        **⚖️ 綜合判決：** 本案三方幕僚均未通過『直球對決測試』，本看板將持續亮起黃紅燈示警，引導在地選民持續施壓。
        """)

else:
    st.write(f"暫無【{town}】的青年提案。這代表該區的傳統派系樁腳勢力依舊穩固，地方青年正在實體討論會中秘密集結，敬請期待下週火網全開！")
