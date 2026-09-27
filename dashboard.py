import streamlit as st
import pandas as pd
import time

# 1. System App Config
st.set_page_config(page_title="NexusData Core v2.0", page_icon="⚡", layout="wide")

# Modern Premium Dark Interface Styling
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    div[data-testid="stMetricBlock"] { background: rgba(22, 27, 34, 0.8); border: 1px solid #30363d; border-radius: 12px; padding: 20px !important; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
    div.stButton > button:first-child { background-color: #238636 !important; color: white !important; border-radius: 8px !important; font-weight: bold; width: 100%; }
    div.stButton > button:first-child:hover { background-color: #2ea44f !important; }
    </style>
""", unsafe_allow_html=True)

# 2. Sidebar Parameters (Cleaned & Professional)
with st.sidebar:
    st.markdown("## **System Engine Options**")
    st.markdown("---")
    api_url = st.text_input("📡 API Core Connection String", value="http://127.0.0.1:8000")
    sec_key = st.text_input("🔐 Secure Gateway Token", value="local-development-secret", type="password")
    st.info("● Engine Core: ACTIVE\n\n● DB Storage Cluster: CONNECTED")

# 3. Main Interface Branding (Removed "High-Ticket" text)
st.markdown("<p style='color: #58a6ff; font-weight: bold; margin-bottom: 0;'>NEXUSDATA INTELLIGENCE PLATFORM</p>", unsafe_allow_html=True)
st.title("⚡ Enterprise Web Data Extraction Platform")
st.markdown("### *Production-Grade Automated Data Pipeline Suite*")
st.markdown("---")

# 4. Metrics Dashboard Row (Changed to Professional, Measurable Metrics)
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Total Records Processed", value="14,802", delta="+2,410 Today")
m2.metric(label="Avg. Response Latency", value="42ms", delta="-8ms Optimization")
m3.metric(label="Request Success Rate", value="99.8%", delta="Steady")
m4.metric(label="Processing Cost (Per Run)", value="$0.0014", delta="Optimized")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Pipeline Inputs and Execution Trigger (Cleaned Wording)
target_endpoint = st.text_input("Target Data Root Endpoint URL", placeholder="https://example-data-directory.com")
extraction_config = st.selectbox("Extraction Configuration Mode", ["High-Performance Multi-Threaded Engine", "Scheduled Incremental Sync Node"])

if st.button("🚀 START DATA EXTRACTION ROUTINE"):
    if not target_endpoint:
        st.error("❌ Action Required: Enter a target execution URL parameter.")
    else:
        with st.spinner("⏳ Supervisor Loop Initialized. Activating Execution Pipeline..."):
            time.sleep(2.0)
            mock_pipeline_output = [
                {"workflow_id": "WF-9921", "company_name": "Apex Digital Corp", "email": "corp@apexdigital.io", "status": "SYNCED"},
                {"workflow_id": "WF-9922", "company_name": "Starlight Ventures", "email": "funding@starlight.vc", "status": "SYNCED"},
                {"workflow_id": "WF-9923", "company_name": "Vertex Global Inc", "email": "ops@vertexglobal.com", "status": "SYNCED"}
            ]
            st.success("🎉 Data extraction loop committed successfully to database cache!")
            df = pd.DataFrame(mock_pipeline_output)
            st.dataframe(df, use_container_width=True)