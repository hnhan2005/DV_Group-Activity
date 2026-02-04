import streamlit as st

st.header("Phân Tích Lợi Nhuận Theo Vùng")

st.info("""
Thời gian: 03/01/2014 - 30/12/2017  
Các vùng được phân tích bao gồm: West, East, South, Central
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **1. Vùng West có lợi nhuận cao nhất:** Lợi nhuận **$108,418.45**, cao hơn gấp **1.18 lần** so với vùng East và chiếm khoảng **38%** tổng lợi nhuận.

    **2. Vùng East nằm ở vị trí thứ hai:** Lợi nhuận **$91,522.78**, hiệu suất tốt và gần bằng vùng West.
    """)

with col2:
    st.markdown("""
    **3. Vùng South:** South có lợi nhuận **$46,749.43** (khoảng **43%** so với West)
        
    **4. Vùng Central:** thấp nhất với **$39,706.36** (khoảng **37%** so với West).
    """)

st.success("""
**Nhận xét:** Khoảng cách giữa hai vùng cao nhất và hai vùng thấp nhất là rất lớn (West cao gấp **2.73 lần** Central). 
Vùng South và Central cần cải thiện lợi nhuận bằng cách phân tích nguyên nhân lợi nhuận thấp, xem xét điều chỉnh giá, chi phí vận chuyển hoặc marketing, và tìm hiểu đặc điểm khách hàng cùng nhu cầu thị trường địa phương. 
Đồng thời, nên duy trì và tập trung phát triển thêm ở hai thị trường lớn nhất.
""")
  