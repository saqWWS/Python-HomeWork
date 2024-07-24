def user(name, surename, message="Hi team!"):
        
    print(f"{name} {surename}: {message}")
        
name = input("Write a name:\t")
surename = input("Write a surename:\t")

user(name, surename)

user("Team", "leader", message=f"Hello! {name} {surename}")
