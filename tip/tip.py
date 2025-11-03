def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    remove_d = d.lstrip("$")
    return float(remove_d)


def percent_to_float(p):
    remove_p = p.rstrip("%")
    fl_remove_p = float(remove_p)
    final = fl_remove_p/100
    return final

main()
