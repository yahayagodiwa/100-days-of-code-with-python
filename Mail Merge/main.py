
PLACEHOLDER = "[name]"
with open(r"Mail Merge\Input\Names\invited_names.txt") as name_file:
      names =  name_file.readlines()
    

with open("Mail Merge\Input\Letters\starting_letter.txt") as letter_file:
      letter_content = letter_file.read()
      for name in names:
            stripe_name = name.strip()
            new_letter = letter_content.replace(PLACEHOLDER, stripe_name)
            with open(f"Mail Merge\\Output\\ReadyToSend\\letter_for_{stripe_name}.txt",
                       mode = "w") as completed:
                  completed.write(new_letter)
