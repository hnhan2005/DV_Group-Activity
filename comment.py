import streamlit as st

st.set_page_config(page_title="Group Activity", layout="wide", initial_sidebar_state="collapsed")

st.header("Phân tích lợi nhuận theo vùng")

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

# pie chart
st.header("Phân tích doanh thu theo danh mục sản phẩm")

st.info("""
Các danh mục được phân tích: Technology, Furniture, Office Supplies
""")

st.markdown("""
    **1. Các mặt hàng công nghệ (Technology) đạt doanh thu cao nhất:** Doanh thu đạt được là **$836,154.03**, chiếm khoảng **36.4%** tổng doanh thu toàn hệ thống. Đây là nhóm hàng mang lại dòng tiền lớn nhất.

    **2. Sản phẩm nội thất (Furniture) đứng thứ hai:** Doanh thu đạt **$741,999.80**, chiếm **32.3%**.
    
    **3. Văn phòng phẩm (Office Supplies):** Đạt **$719,047**, chiếm **31.3%** và gần bằng doanh thu của Furniture. Chênh lệch doanh thu khi so với nhóm cao nhất (Technology) là không quá lớn (với doanh thu của Technology gấp **1.16 lần**).
""")

st.success("""
**Nhận xét:** Cơ cấu doanh thu giữa 3 nhóm ngành hàng khá cân bằng (đều xoay quanh mức 31-36%). Điều này cho thấy sự ổn định về doanh thu của đa dạng sản phẩm trong hệ thống khi không bị quá phụ thuộc vào một nhóm ngành hàng nào.
* **Technology:** Là mặt hàng chủ chốt của hệ thống Superstore, cần ưu tiên quảng bá cho các sản phẩm công nghệ mới cũng như đẩy mạnh các chương trình ưu đãi để duy trì vị thế dẫn đầu.
* **Furniture:** Doanh thu tốt nhưng cần kiểm soát chặt lợi nhuận vì rủi ro về chi phí vận chuyển cao, có thể mang lại lợi nhuận thấp hoặc âm.
* **Office Supplies:** Tuy doanh thu ít nhất nhưng đây là sản phẩm thiết yếu với nhu cầu mua sắm thường xuyên, nên có thể triển khai các chiến lược bán theo combo thay vì bán lẻ để tăng giá trị doanh thu.
""")