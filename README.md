# Hướng dẫn chạy phần mềm

## 1. Install tools
- python 2.1.15
- Django 5.1.6
- SQL Server 2017

có thể  tham khảo tại [Link install-tool.md](install-tool.md)

## 2. Giải nén và chạy migrations
giải nén sau đó

```bash 
cd myproject
```

Chạy lệnh migrate
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

## 3. Khởi tạo Employee stored procedure
Truy cập [Link myproject/sql/employee.sql](myproject/sql/employee.sql)
Chạy lệnh trên sqlserver 2017

## 4. Tạo super user
```bash
python manage.py createsuperuser
```

## 5. Chạy server
```bash
python manage.py runserver
```


