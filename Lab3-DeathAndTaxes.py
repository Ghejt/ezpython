def main():
    status = input("Enter Marital Status:")
    income = int(input("Enter Income:"))
    
    def is_valid(status, income):
        status = status.lower()
        if status == 'single':
            valid = True
        elif status == 'married':
            valid =  True
        elif status == 'married filing jointly':
            valid = True
        elif status == 'married filing separately':
            valid = True
        elif status == 'widow(er)':
            valid = True
        elif status == 'head of household':
            valid = True
        else:
            valid = False
            print("Status must be: 'Single', 'Married', 'Married filing separately', 'Widow', 'Widower' or  'Head of household'.")

    is_valid(status, income)

    def get_tax(status, income):
        status = status.lower()
        if status == "married" or status == "widow" or status == "widower":
            if income <= 18650.99:
                tax = int(.10 * income)
            elif income >= 18651 and income <= 75900.99:
                tax = int((.15 * (income -  18650)) + 1865)
            elif income >= 75901 and income <= 153100.99:
                tax = int((.25 * (income - 75900)) + 13250)
            elif income >= 153101 and income <= 233350.99:
                tax = int((.28 * (income - 153100)) + 32549)
            elif income >= 233351 and income <= 416700.99:
                tax = int((.33 * (income - 233350)) + 55019)
            elif income >= 416701 and income <= 470700.99:
                tax = int((.35 * (income - 416701)) + 115525)
            elif income >= 470701:
                tax = int((.396 * (income - 470700)) + 134325)
            else:
                return "Invalid. Your income isn't real."
            return tax
        elif status == "single":
            if income <= 9325.99:
                tax = int(.10 * income)
            elif income >= 9326 and income <= 37950.99:
                tax = int((.15 * (income - 9325)) + 933)
            elif income >= 37951 and income <= 91900.99:
                tax = int((.25 * (income - 37950)) + 5227)
            elif income >= 91901 and income <= 191650.99:
                tax = int((.28 * (income - 91900)) + 21214)
            elif income >= 191651 and income <= 416700.99:
                tax = int((.33 * (income - 191650)) + 49144)
            elif income >= 416701 and income <= 418400.99:
                tax = int((.35 * (income - 416700)) + 123410)
            elif income >= 418401:
                tax = int((.396 * (income - 418400)) + 124005)
            return tax
        elif status == 'married filing separately':
            if income <= 9325.99:
                tax = int(.10 * income)
            elif income >= 9326 and income <= 37950.99:
                tax = int((.15 * (income - 9325)) + 933)
            elif income >= 37951 and income <= 76550.99:
                tax = int((.25 * (income - 37950)) + 5227)
            elif income >= 76551 and income <= 116675.99:
                tax = int((.28 * (income - 76551)) + 14876)
            elif income >= 116676 and income <= 208350.99:
                tax = int((.33 * (income - 116675)) + 26111)
            elif income >= 208351 and income <= 235350.99:
                tax = int((.35 * (income - 208350)) + 56363)
            elif income >= 235351:
                tax = int((.396 * (income - 235350)) + 65813)
            else:
                return "Invalid. Your income isn't real."
            return tax
        elif status == 'head of household':
            if income <= 13350.99:
                tax = int(.10 * income)
            elif income >= 13351 and income <= 50800.99:
                tax = int((.15 * (income - 13350)) + 1335)
            elif income >= 50801 and income <= 131200.99:
                tax = int((.25 * (income - 50800)) + 6952)
            elif income >= 131201 and income <= 212500.99:
                tax = int((.28 * (income - 131200)) + 27052)
            elif income >= 212501 and income <= 416700.99:
                tax = int((.33 * (income - 212500)) + 49816)
            elif income >= 416701 and income <= 444500.99:
                tax = int((.35 * (income - 416700)) + 117201)
            elif income >= 444501:
                tax = int((.396 * (income - 444501)) + 126931)
            else:
                return "Invalid. Your income isn't real."
            return tax
        else:
            print("Invalid syntax. Type either 'Married', 'Single', 'Head of household', or 'Married filing separately'")
            exit()

    tax = get_tax(status, income)

    def percent_of_income(tax, income):
        return float((tax/income) * 100)

    percent = percent_of_income(tax, income)

    print("Tax: $" + str(tax))
    print("Percent of income: " + str(percent) + "%")
        
