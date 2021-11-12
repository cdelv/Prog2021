def BMI(m,h):
	return m/(h*h)


def findBMI(pairs):
        answer = []
        for pair in range(pairs):
                m,h = input().split()
                bmi = BMI(float(m), float(h))

                if bmi < 18.5:
                    answer.append(str('under'))
                elif bmi >= 18.5 and bmi < 25.0:
                    answer.append(str('normal'))
                elif bmi >= 25.0 and bmi < 30.0:
                    answer.append(str('over'))
                elif bmi >= 30.0:
                    answer.append(str('obese'))
                else:
                    print("Error.")

        print(' '.join(answer))


findBMI(int(input()))