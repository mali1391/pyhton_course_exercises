Python Exception Handling Exercises
====================================

The following 10 exercises are arranged from intermediate to advanced.
All exercises are in English.

LEVEL 1 - INTERMEDIATE
----------------------

Exercise 1: Safe Division
Write a Python program that asks the user to enter two numbers and divides the first number by the second number.

Requirements:
- Handle ZeroDivisionError if the second number is zero.
- Handle ValueError if the user enters something other than a valid number.
- Display an appropriate error message for each exception.
- Use a finally block to print "Operation completed."


Exercise 2: File Reader
Write a program that asks the user to enter a filename and reads its contents.

Requirements:
- Handle FileNotFoundError if the file does not exist.
- Handle PermissionError if the program does not have permission to read the file.
- Handle other unexpected exceptions using a general Exception block.
- Display the file contents if the operation is successful.


Exercise 3: List Index Access
Create a list containing at least 5 elements.

Ask the user to enter an index and display the corresponding element.

Requirements:
- Handle ValueError if the input is not an integer.
- Handle IndexError if the index is outside the valid range.
- Use else to display a success message when no exception occurs.


LEVEL 2 - UPPER INTERMEDIATE
----------------------------

Exercise 4: Student Grade Calculator
Write a program that asks the user to enter the grades of 5 students.

Requirements:
- Each grade must be a number between 0 and 20.
- Handle ValueError for invalid numerical inputs.
- Raise a ValueError if a grade is outside the allowed range.
- Calculate and display the average grade.
- If an invalid grade is entered, ask the user to enter it again.


Exercise 5: Bank Account Withdrawal
Create a BankAccount class with the following attributes and methods:

Attributes:
- account_number
- balance

Methods:
- deposit(amount)
- withdraw(amount)

Requirements:
- Raise a ValueError if the deposit or withdrawal amount is negative or zero.
- Raise a custom InsufficientBalanceError if the withdrawal amount exceeds the current balance.
- Handle all exceptions appropriately when calling these methods.
- The account balance must never become negative.


Exercise 6: JSON Configuration Reader
Write a program that reads configuration data from a JSON file.

Example JSON structure:

{
    "username": "admin",
    "password": "123456",
    "port": 8080,
    "debug": true
}

Requirements:
- Handle FileNotFoundError if the file does not exist.
- Handle json.JSONDecodeError if the JSON format is invalid.
- Check whether all required keys exist.
- Raise a custom exception called MissingConfigurationError if a required key is missing.
- Display the configuration if everything is valid.


LEVEL 3 - ADVANCED
------------------

Exercise 7: Login System
Implement a simple login system.

Requirements:
- Store at least 3 usernames and passwords in a dictionary.
- Ask the user to enter their username and password.
- Raise a custom InvalidUsernameError if the username does not exist.
- Raise a custom InvalidPasswordError if the password is incorrect.
- Allow only 3 login attempts.
- Use try-except-else-finally appropriately.
- Display a message when the user successfully logs in or runs out of attempts.


Exercise 8: CSV Data Processor
Write a program that reads a CSV file containing student information.

Example CSV file:

name,age,grade
John,20,18
Alice,22,17
Bob,invalid,15
David,19,21

Requirements:
- Handle FileNotFoundError if the file does not exist.
- Handle invalid CSV data.
- Validate that:
  - age is a valid integer.
  - grade is a number between 0 and 20.
  - name is not empty.
- If a row contains invalid data, skip that row and continue processing the remaining rows.
- Display all valid student records.
- Display the number of valid and invalid records.


Exercise 9: ATM Simulation
Develop a simple ATM simulation program.

Requirements:
- The user starts with a balance of 1000.
- Provide the following operations:
  1. Check balance
  2. Deposit money
  3. Withdraw money
  4. Exit
- Handle invalid menu selections.
- Handle invalid numerical inputs.
- Raise custom exceptions for:
  - Insufficient balance.
  - Invalid transaction amount.
  - Maximum daily withdrawal limit exceeded.
- The maximum daily withdrawal limit is 500.
- The program must continue running even if an operation fails.
- Use multiple except blocks to handle different exceptions.


LEVEL 4 - CHALLENGE
-------------------

Exercise 10: Robust Data Import System
Develop a program that imports user information from a JSON file and stores it in a Python list of dictionaries.

Example JSON file:

[
    {
        "id": 1,
        "name": "John",
        "age": 25,
        "email": "john@example.com"
    },
    {
        "id": 2,
        "name": "Alice",
        "age": "invalid",
        "email": "alice@example.com"
    },
    {
        "id": 3,
        "name": "Bob",
        "age": 30,
        "email": "bob@example.com"
    }
]

Requirements:
- Handle FileNotFoundError.
- Handle json.JSONDecodeError.
- Validate every user's information:
  - id must be a positive integer.
  - name must not be empty.
  - age must be an integer between 1 and 120.
  - email must contain @.
- Create custom exceptions for invalid user data.
- If one user's information is invalid, skip that user and continue processing the remaining users.
- Keep track of valid and invalid records.
- Use try-except-else-finally.
- At the end, display a complete processing report.


STUDENT NOTE
------------

In all exercises, try to use the following structures where appropriate:

try:
    # Code that may raise an exception

except ValueError:
    # Handle invalid values

except FileNotFoundError:
    # Handle missing files

except Exception as e:
    # Handle unexpected exceptions

else:
    # Execute if no exception occurs

finally:
    # Always execute


IMPORTANT:
Catching exceptions is not enough. You should understand when to raise an exception yourself and when to handle an exception raised by Python or another function.

Suggested exercises for assessing practical understanding:
Exercises 5, 8, 9, and 10.

تمرین‌های مدیریت استثناها در پایتون
====================================

۱۰ تمرین زیر از سطح متوسط ​​تا پیشرفته تنظیم شده‌اند.
تمامی تمرین‌ها به زبان انگلیسی هستند.

سطح ۱ - متوسط
----------------------

تمرین ۱: تقسیم ایمن
برنامه‌ای به زبان پایتون بنویسید که از کاربر بخواهد دو عدد وارد کند و عدد اول را بر عدد دوم تقسیم نماید.

الزامات:
- در صورتی که عدد دوم صفر بود، خطای `ZeroDivisionError` را مدیریت کنید.
- اگر کاربر مقداری غیر از یک عدد معتبر وارد کرد، خطای `ValueError` را مدیریت کنید.
- برای هر استثنا، یک پیام خطای مناسب نمایش دهید.
- از یک بلوک `finally` برای چاپ عبارت "Operation completed." (عملیات تکمیل شد) استفاده کنید.


تمرین ۲: خواندن فایل
برنامه‌ای بنویسید که از کاربر نام فایلی را دریافت کرده و محتوای آن را بخواند.

الزامات:
- اگر فایل وجود نداشت، خطای `FileNotFoundError` را مدیریت کنید.
- اگر برنامه اجازه خواندن فایل را نداشت، خطای `PermissionError` را مدیریت کنید.
- سایر استثناهای غیرمنتظره را با استفاده از یک بلوک کلی `Exception` مدیریت نمایید.
- در صورت موفقیت‌آمیز بودن عملیات، محتوای فایل را نمایش دهید.


تمرین ۳: دسترسی به عناصر لیست از طریق ایندکس
لیستی ایجاد کنید که حداقل شامل ۵ عنصر باشد.

از کاربر بخواهید یک ایندکس (شاخص) وارد کند و عنصر متناظر با آن را نمایش دهید.

الزامات:
- اگر ورودی عدد صحیح (integer) نبود، خطای `ValueError` را مدیریت کنید.
- اگر ایندکس وارد شده خارج از محدوده مجاز بود، خطای `IndexError` را مدیریت کنید.
- از بلوک `else` استفاده کنید تا در صورتی که هیچ استثنایی رخ نداد، پیام موفقیت نمایش داده شود.


سطح ۲ - متوسط ​​رو به بالا
----------------------------

تمرین ۴: محاسبه نمرات دانش‌آموزان
برنامه‌ای بنویسید که نمرات ۵ دانش‌آموز را از کاربر دریافت کند.

الزامات:
- هر نمره باید عددی بین ۰ تا ۲۰ باشد.
- برای ورودی‌های عددی نامعتبر، خطای `ValueError` را مدیریت کنید.
- اگر نمره‌ای خارج از محدوده مجاز بود، یک خطای `ValueError` ایجاد (raise) کنید.
- میانگین نمرات را محاسبه کرده و نمایش دهید.
- در صورتی که نمره نامعتبری وارد شد، از کاربر بخواهید دوباره آن را وارد کند.

تمرین ۵: برداشت از حساب بانکی
کلاسی به نام `BankAccount` با ویژگی‌ها و متدهای زیر ایجاد کنید:

ویژگی‌ها (Attributes):
- `account_number` (شماره حساب)
- `balance` (موجودی حساب)

متدها (Methods):
- `deposit(amount)` (واریز مبلغ)
- `withdraw(amount)` (برداشت مبلغ)

الزامات:
- اگر مبلغ واریز یا برداشت منفی یا صفر باشد، یک خطای `ValueError` ایجاد (raise) کنید.
- اگر مبلغ برداشت بیشتر از موجودی فعلی باشد، یک خطای سفارشی به نام `InsufficientBalanceError` ایجاد کنید.
- هنگام فراخوانی این متدها، تمام استثناها (exceptions) را به درستی مدیریت کنید.
- موجودی حساب هرگز نباید منفی شود.


تمرین ۶: خواننده تنظیمات JSON
برنامه‌ای بنویسید که داده‌های پیکربندی (تنظیمات) را از یک فایل JSON بخواند.

نمونه ساختار JSON:

{
"username": "admin",
"password": "123456",
"port": 8080,
"debug": true
}

الزامات:
- اگر فایل وجود نداشت، خطای `FileNotFoundError` را مدیریت کنید.
- اگر فرمت JSON نامعتبر بود، خطای `json.JSONDecodeError` را مدیریت کنید.
- بررسی کنید که آیا تمام کلیدهای مورد نیاز وجود دارند یا خیر.
- اگر یکی از کلیدهای ضروری وجود نداشت، یک خطای سفارشی به نام `MissingConfigurationError` ایجاد کنید.
- اگر همه چیز معتبر بود، تنظیمات را نمایش دهید.


سطح ۳ - پیشرفته
------------------

تمرین ۷: سیستم ورود (Login)
یک سیستم ورود ساده پیاده‌سازی کنید.

الزامات:
- حداقل ۳ نام کاربری و رمز عبور را در یک دیکشنری (dictionary) ذخیره کنید.
- از کاربر بخواهید نام کاربری و رمز عبور خود را وارد کند.
- اگر نام کاربری وجود نداشت، یک خطای سفارشی به نام `InvalidUsernameError` ایجاد کنید.
- اگر رمز عبور نادرست بود، یک خطای سفارشی به نام `InvalidPasswordError` ایجاد کنید.
- تنها اجازه ۳ بار تلاش برای ورود را بدهید.
- از ساختار `try-except-else-finally` به درستی استفاده کنید.
- زمانی که کاربر با موفقیت وارد شد یا تعداد دفعات تلاش او به پایان رسید، پیامی نمایش دهید.


تمرین ۸: پردازشگر داده‌های CSV
برنامه‌ای بنویسید که یک فایل CSV حاوی اطلاعات دانشجویان را بخواند.

نمونه فایل CSV:

name,age,grade
John,20,18
Alice,22,17
Bob,invalid,15
David,19,21

الزامات:
- اگر فایل وجود نداشت، خطای `FileNotFoundError` را مدیریت کنید. - داده‌های نامعتبر در فایل CSV را مدیریت کنید.
- اعتبارسنجی کنید که:
- سن (age) یک عدد صحیح معتبر باشد. 
- نمره (grade) عددی بین ۰ تا ۲۰ باشد.
- نام (name) خالی نباشد.
- اگر سطری حاوی داده‌های نامعتبر بود، آن سطر را نادیده بگیرید و پردازش سطرهای باقی‌مانده را ادامه دهید.
- تمام رکوردهای معتبر دانش‌آموزان را نمایش دهید.
- تعداد رکوردهای معتبر و نامعتبر را نمایش دهید.


تمرین ۹: شبیه‌سازی دستگاه خودپرداز (ATM)
برنامه‌ای ساده برای شبیه‌سازی عملکرد یک دستگاه خودپرداز (ATM) بنویسید.

نیازمندی‌ها:
- موجودی اولیه کاربر ۱۰۰۰ واحد است.
- عملیات زیر را فراهم کنید:
۱. مشاهده موجودی
۲. واریز وجه
۳. برداشت وجه
۴. خروج
- انتخاب‌های نامعتبر در منو را مدیریت کنید.
- ورودی‌های عددی نامعتبر را مدیریت کنید.
- برای موارد زیر، استثناهای (Exceptions) سفارشی تعریف و ایجاد کنید:
- موجودی ناکافی. 
- مبلغ تراکنش نامعتبر. 
- فراتر رفتن از سقف برداشت روزانه.
- سقف برداشت روزانه ۵۰۰ واحد است.
- برنامه باید حتی در صورت شکست یک عملیات، به اجرای خود ادامه دهد.
- برای مدیریت استثناهای مختلف، از چندین بلوک `except` استفاده کنید.


سطح ۴ - چالش
-------------------

تمرین ۱۰: سیستم واردسازی داده‌های مقاوم (Robust)
برنامه‌ای بنویسید که اطلاعات کاربران را از یک فایل JSON وارد کرده و آن‌ها را در یک لیست پایتونی شامل دیکشنری‌ها ذخیره کند.

نمونه فایل JSON:

[
{
"id": 1,
"name": "John",
"age": 25,
"email": "john@example.com"
},
{
"id": 2,
"name": "Alice",
"age": "invalid",
"email": "alice@example.com"
},
{
"