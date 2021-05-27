PLACEHOLDER = "[name]"

with open("../mail_merge_script/Input/Names/invited_names.txt", mode = "r") as names:
    all_names = names.readlines()
with open("../mail_merge_script/Input/Letters/starting_letter.txt", mode="r") as mails:
    new_letter = mails.read()
    # print(all_names)
    # print(new_letter)
    for name in all_names:
        stripped_name = name.strip()
        new_mail = new_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"../mail_merge_script/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w") as ready_files:
            ready_files.write(new_mail)