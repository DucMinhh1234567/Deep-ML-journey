2. np.array(gradient, dtype=float)
- **Mục đích**: Chuyển list Python về mảng NumPy (kiểu float) để:
  - Tận dụng được các phép toán vector hoá (vectorized operations).
  - Dùng các hàm tuyến tính như `np.linalg.norm`, cộng trừ nhân chia từng phần tử.

3. np.linalg.norm(gradient)
- **Mục đích**: Tính L2 norm (độ lớn/ magnitude) của vector:
  - Tương đương \(\sqrt{\sum_i g_i^2}\).
  - Dùng để tính độ dốc của hàm mất mát tại một điểm (độ lớn gradient).

4. np.zeros_like(gradient)
- **Mục đích**: Tạo vector 0 có cùng shape và dtype với `gradient`.
- **Ứng dụng**: Xử lý edge case gradient = 0:
  - Tránh chia cho 0 khi chuẩn hoá.
  - Giữ đúng kích thước vector nhưng tất cả phần tử đều bằng 0.

5. Vectorized operations với mảng NumPy
- **Ví dụ**:
  - `direction = gradient / magnitude`
  - `descent_direction = -direction`
- **Mục đích**:
  - Tính toán trên toàn bộ vector cùng lúc, nhanh và gọn hơn vòng lặp for.
  - Rất quan trọng trong ML vì gradient có thể có dimension rất lớn.

6. np.convolve(f_coeffs, g_coeffs)
- **Mục đích**: Tính tích chập (convolution) hai dãy hệ số đa thức:
  - Dùng để nhân hai đa thức: nếu `f(x)` và `g(x)` có hệ số lần lượt là `f_coeffs`, `g_coeffs`,
    thì hệ số của \(f(x) \cdot g(x)\) chính là `np.convolve(f_coeffs, g_coeffs)`.
- **Liên hệ giải tích**:
  - Trong quy tắc tích (product rule), phần `f'(x)g(x)` và `f(x)g'(x)` đều có thể biểu diễn bằng nhân đa thức, nên `np.convolve` rất hữu ích.

7. np.polyval(coeffs, x)
- **Mục đích**: Tính giá trị đa thức tại điểm \(x\).
- **Cách dùng**:
  - `coeffs` là hệ số theo thứ tự bậc giảm dần, ví dụ `[1, 2, 3]` tương ứng \(x^2 + 2x + 3\).
  - `np.polyval([1, 2, 3], 2.0)` sẽ tính \(2^2 + 2\cdot2 + 3\).
- **Ứng dụng**:
  - Tính \(g(x)\), \(h(x)\) trong quy tắc thương (quotient rule) cho đa thức.

8. np.polyder(coeffs)
- **Mục đích**: Lấy hệ số đạo hàm của đa thức.
- **Ví dụ**:
  - `coeffs = [1, 0, 1]` tương ứng \(x^2 + 1\).
  - `np.polyder(coeffs)` cho `[2, 0]` tương ứng \(2x\).
- **Ứng dụng**:
  - Dùng để tính \(g'(x)\), \(h'(x)\) nhanh, thay vì tự viết vòng lặp tính đạo hàm.

9. Kết hợp np.polyval và np.polyder trong quy tắc thương
- **Mẫu sử dụng**:
  - `gx = np.polyval(g_coeffs, x)`  -> \(g(x)\)
  - `hx = np.polyval(h_coeffs, x)`  -> \(h(x)\)
  - `g_der = np.polyder(g_coeffs)`  -> hệ số \(g'(x)\)
  - `h_der = np.polyder(h_coeffs)`  -> hệ số \(h'(x)\)
  - `gpx = np.polyval(g_der, x)`    -> \(g'(x)\)
  - `hpx = np.polyval(h_der, x)`    -> \(h'(x)\)
- **Sau đó áp dụng**:
  - \(f'(x) = \dfrac{g'(x)h(x) - g(x)h'(x)}{[h(x)]^2}\)