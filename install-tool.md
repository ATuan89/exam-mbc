# Cài đặt Python 3.10.5, SQL Server 2017 và Django 2.1.15 trên Ubuntu 20.04

## 1. Cài đặt Python 3.10.5

### Bước 1: Cập nhật hệ thống

```bash
sudo apt update && sudo apt upgrade -y
```

### Bước 2: Cài đặt các gói phụ thuộc

Cài đặt các thư viện cần thiết để biên dịch Python.

```bash
sudo apt install -y software-properties-common build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev curl libbz2-dev
```

### Bước 3: Tải Python 3.10.5
```bash
wget https://www.python.org/ftp/python/3.10.5/Python-3.10.5.tgz
tar -xzf Python-3.10.5.tgz
cd Python-3.10.5
```

### Bước 4: Biên dịch và cài đặt Python

Biên dịch Python từ mã nguồn và cài đặt.

```bash
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
```

### Bước 5: Kiểm tra phiên bản Python

Xác nhận Python 3.10.5 đã được cài đặt.

```bash
python3.10 --version
```

### Bước 6: Cài đặt pip

Tải và cài đặt pip cho Python 3.10.5.

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py
```

Kiểm tra phiên bản pip:

```bash
pip3.10 --version
```

## 2. Cài đặt SQL Server 2017

### Bước 1: Thêm kho lưu trữ của Microsoft

```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2017.list | sudo tee /etc/apt/sources.list.d/mssql-server-2017.list
```

### Bước 2: Cập nhật và cài đặt SQL Server

```bash
sudo apt update
sudo apt install -y mssql-server
```

### Bước 3: Cấu hình SQL Server

Chạy script cấu hình để thiết lập SQL Server.

```bash
sudo /opt/mssql/bin/mssql-conf setup
```

- Đặt mật khẩu cho tài khoản SA (yêu cầu ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt).

### Bước 4: Kiểm tra trạng thái SQL Server

Xác nhận SQL Server đang chạy.

```bash
systemctl status mssql-server
```

## 3. Cài đặt Django 2.1.15 trên môi trường ảo

### Bước 1: Cài đặt virtualenv

Cài đặt công cụ để tạo môi trường ảo.

```bash
sudo pip3.10 install virtualenv
```

### Bước 2: Tạo và kích hoạt môi trường ảo

Truy cấp thư mục dự án và môi trường ảo.

```bash
cd exam-mbc
virtualenv -p python3.10 venv
source venv/bin/activate
```

### Bước 3: Cài đặt Django 2.1.15 và các gói cần thiết

Cài đặt Django trong môi trường ảo.

```bash
pip install django==2.1.15 django-pyodbc-azure==2.1.0.0 pyodbc
```

Kiểm tra phiên bản Django:

```bash
django-admin --version
```

## Lý do không sử dụng Django 5.1.6
- Việc sử dụng Django 5.1.6 sẽ dẫn đến lỗi ResolutionImpossible khi cài đặt, vì django-pyodbc-azure không hỗ trợ các phiên bản Django mới hơn 2.1.x.
- Để đảm bảo tính tương thích với SQL Server thông qua django-pyodbc-azure, chúng ta chọn Django 2.1.15, phiên bản cuối cùng trong chuỗi 2.1.x, cho phép sử dụng các tính năng cần thiết mà không gặp xung đột phụ thuộc.