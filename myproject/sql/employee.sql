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