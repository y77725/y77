import streamlit as st

st.title("🕶学生 杨元源-数字档案",anchor='sixth')
st.title("🔑基础信息",anchor='four')
st.text("学号ID:23051170130")

st.header('注册时间: :green[2023-10-01 08:30:17] |精神状态: ✅ 正常 ',anchor='one')
st.header('当前教师: :green[实训301] |精神状态: ✅ 绝密 ',anchor='one')

st.header("🧠 技能矩阵")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Python 编程", "95%", "5%")
with col2:
    st.metric("Streamlit 开发", "87%", "3%")
with col3:
    st.metric("科幻创意", "68%", "-2%")
st.header("📜 任务日志")

st.header("Streamlit课程进度")
st.write("Streamlit课程进度")
st.progress(0.5)  # 模拟进度条

task_data = {
    "日期": ["2023-10-01", "2023-10-05", "2023-10-12"],
    "任务": ["学生数字档案", "课程管理系统", "数据图表展示"],
    "状态": ["✅ 完成", "🔄 进行中", "❌ 未完成"],
    "难度": ["⭐⭐⭐☆☆", "⭐⭐⭐☆☆", "⭐⭐⭐⭐☆"]
}

# 任务日志表格
st.header("任务日志")
st.table(task_data)


st.header("💻 最新代码成果")
code = """
def cosmic_navigation():
    print("启动宇宙导航程序...")
    # 科幻导航算法实现
    return "导航坐标已生成"

result = cosmic_navigation()
print(result)
"""
st.code(code, language="python")

import streamlit as st

st.markdown(
    """
    >> SYSTEM MESSAGE: 下一个任务目标已解锁...  
    >> TARGET: 课程管理系统  
    >> COUNTDOWN: 2025-06-03 15:24:58  
    系统状态: 在线 连接状态: 已加密  
    """,
    unsafe_allow_html=False
)
