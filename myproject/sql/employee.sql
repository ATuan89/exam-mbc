-- Stored Procedure for Inserting an Employee
CREATE PROCEDURE sp_InsertEmployee
    @employee_code VARCHAR(10),
    @employee_first_name VARCHAR(50),
    @employee_last_name VARCHAR(50),
    @gender TINYINT,
    @department_code VARCHAR(10),
    @job_code VARCHAR(10),
    @birthday DATE
AS
BEGIN
    INSERT INTO employees (
        employee_code, employee_first_name, employee_last_name, 
        gender, department_code, job_code, birthday, valid
    )
    VALUES (@employee_code, @employee_first_name, @employee_last_name, 
            @gender, @department_code, @job_code, @birthday, 1)
END
GO

-- Stored Procedure for Updating an Employee
CREATE PROCEDURE sp_UpdateEmployee
    @employee_id INT,
    @employee_code VARCHAR(10),
    @employee_first_name VARCHAR(50),
    @employee_last_name VARCHAR(50),
    @gender TINYINT,
    @department_code VARCHAR(10),
    @job_code VARCHAR(10),
    @birthday DATE
AS
BEGIN
    UPDATE employees
    SET employee_code = @employee_code,
        employee_first_name = @employee_first_name,
        employee_last_name = @employee_last_name,
        gender = @gender,
        department_code = @department_code,
        job_code = @job_code,
        birthday = @birthday
    WHERE employee_id = @employee_id AND valid = 1
END
GO

-- Stored Procedure for Deleting an Employee (Soft Delete)
CREATE PROCEDURE sp_DeleteEmployee
    @employee_id INT
AS
BEGIN
    UPDATE employees
    SET valid = 0
    WHERE employee_id = @employee_id
END
GO


-- Insert Sample Data into departments
INSERT INTO departments (department_code, department_name, valid)
VALUES 
    ('0001', 'Human Resources', 1),
    ('0002', 'Information Technology', 1),
    ('0003', 'Sales', 1),
    ('0004', 'Marketing', 1);

-- Insert Sample Data into jobs
INSERT INTO jobs (job_code, job_name, valid)
VALUES 
    ('0001', 'Manager', 1),
    ('0002', 'Developer', 1),
    ('0003', 'Sales Representative', 1),
    ('0004', 'Marketing Specialist', 1);

-- Insert Sample Data into employees
INSERT INTO employees (employee_code, employee_first_name, employee_last_name, gender, department_code, job_code, birthday, valid)
VALUES 
    ('EMP001', 'Anh', 'Tuan', 1, '0001', '0001', '2000-08-19', 1),
    ('EMP002', 'Nguyen', 'Van', 0, '0002', '0002', '2002-08-22', 1),
    ('EMP003', 'Tai', 'Nguyen', 1, '0003', '0003', '1998-03-10', 1),
    ('EMP004', 'Emily', 'Brown', 0, '0004', '0004', '1995-11-30', 1);