Cài đặt thư viện Django
    - install python
    - cmd -> pip install Django
Cách tạo project Django mới
    vào thư mục muốn lưu -> cmd -> gõ lệnh django-admin startproject <nameproject>
Cấu trúc Django:
    __init__.py: đây là 1 file cơ bản trong Python dùng để biến folder chứa nó thành           package, giúp tao có thể import
    setttings.py: đây là file cấu hình project. (VD: cấu hình database, đặt múi giờ, cài thêm thư viện, ...)
    urls.py: đây là file giúp chúng ta tạo các đường dẫn urls của trang web để liên kết các    webpage lại với nhau
    wsgi.py: đây là file giúp chúng ta deploy project lên server
Cách chạy web trên localhost
    terminal -> python manage.py runserver
    localhost:8000/admin (đén trang đăng nhập)
    localhost:8000/painting (đến trang chủ web)
Tạo app từ project:
    python manage.py startapp <name_app>
