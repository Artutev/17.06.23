#1
def main():
    numbers = []

    while True:
        try:
            num = float(input())
            numbers.append(num)

            if sum(numbers) == 0:
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    sum_of_squares = sum(x ** 2 for x in numbers)
    print(sum_of_squares)


if __name__ == "__main__":
    main()



#2
def main():
    grades = list(map(int, input().split()))
    count_5 = grades.count(5)
    count_4 = grades.count(4)
    count_3 = grades.count(3)
    count_2 = grades.count(2)
    average_grade = sum(grades) / len(grades)
    print(f"{count_5} {count_4} {count_3} {count_2}")
    print(f"{average_grade:.2f}")

if __name__ == "__main__":
    main()



#3
def main():
    grades_input = input().split()
    grades_output = [str(3) if grade == '2' else grade for grade in grades_input]
    print(" ".join(grades_output))

if __name__ == "__main__":
    main()
