def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'
def main():
    try:
        with open('scores.txt', 'r') as file:
            lines = file.readlines()
        # เตรียมไฟล์เพื่อเก็บเกรด
        with open('grades.txt', 'w') as output_file:
            for line in lines:
                # แยกชื่อนักเรียนและคะแนน
                parts = line.strip().split()
                if len(parts) == 2:
                    name, score = parts[0], int(parts[1])
                    # คำนวณเกรด
                    grade = calculate_grade(score)
                    # เขียนลงไฟล์
                    output_file.write(f'{name} {grade}\n')
                else:
                    print(f"Invalid line: {line}")
        print("การคำนวณเกรดเสร็จสมบูรณ์ ผลลัพธ์บันทึกไว้ในไฟล์ grades.txt")
    except FileNotFoundError:
        print("ไฟล์ scores.txt ไม่พบ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
if __name__ == "__main__":
    main()
