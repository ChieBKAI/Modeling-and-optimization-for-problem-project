1. TỔNG QUAN CÁC FILE VÀ FOLDER
 - running_time csv: Folder gồm các file csv chứa dữ liệu về running time của mỗi thuật toán.
 - images: Folder gồm các file png chứa hình ảnh về các biểu đồ và graph.
 - memory_runtime_check: File python chứa source code dùng để tính thời gian và dung lượng bộ nhớ tiêu tốn của thuật toán.
 - MODEL: File ipynb chứa phần tạo graph và demo model với grid 3x3.
 - plot_runtime: File dùng để tạo ra biểu đồ so sánh running time của các thuật toán.

2. THỰC THI FILE MODEL
Để sử dụng được file MODEL thì trước tiên phải cần cài đặt thư viện networkx và matplotlib trong python.
Nếu bạn chưa có thì hãy cài đặt thông qua cmd với trình cài đặt pip thông qua lệnh sau: 
"pip install networkx" và "pip install matplotlib".

3. RUNNING TIME VÀ BỘ NHỚ 
Với mỗi cấu hình máy và trình biên dịch khác nhau thì running time và bộ nhớ tiêu tốn của mỗi thuật toán có thể khác với dữ liệu trong bài.
Mục tiêu cuối cùng của phần tính toán running time và bộ nhớ là để cho việc so sánh.

4. DEMO VỚI GRID 3X3
Ở trong file MODEL chúng mình đã kiểm thử thuật toán với mạng lưới grid 3x3, có source và sink node được nối trực tiếp với những node nằm trên 2 cạnh trên và dưới của grid (xem hình để biết thêm chi tiết). Các thông số như capacity, weight(run time on link) được tạo ngẫu nhiên với hàm random của python, thông số demand được tạo với giá trị là [15 * "số node trên 1 cạnh của grid"] (đọc code để biết thêm chi tiết).
