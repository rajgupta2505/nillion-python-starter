from nada_dsl import *

def nada_main():
    new_member = Party(name="NewMember")

    team_codes = {
        "NEXTGEN000": "NextGen",
        "GOA123": "Goa Coders",
        "BEACH456": "Beach Hackers",
        "SUN789": "Sunset Developers",
        "SURF321": "Surf Programmers",
        "PARTY654": "Party Debuggers",
    }

    secret_team_codes = {code: SecretInteger(code) for code in team_codes.keys()}
    team_code_input = SecretInteger(Input(name="team_code", party=new_member))

    joined_team = SecretInteger(0)

    welcome_messages = {
        "NEXTGEN000": "Welcome to NextGen! Join the future of coding. Your challenge: Innovate with a groundbreaking Web3 project!",
        "GOA123": "Welcome to the Goa Coders! Get ready to code with the waves in the background. Your challenge: Create an app that helps tourists navigate Goa!",
        "BEACH456": "Welcome to the Beach Hackers! Enjoy the sand and the code. Your challenge: Build a beach cleanup scheduling app!",
        "SUN789": "Welcome to the Sunset Developers! Code while enjoying beautiful sunsets. Your challenge: Develop a sunset photo sharing platform!",
        "SURF321": "Welcome to the Surf Programmers! Ride the waves of code. Your challenge: Create a surf forecast app!",
        "PARTY654": "Welcome to the Party Debuggers! Debug with a party vibe. Your challenge: Make a party planning app!",
    }

    rsvp_input = SecretInteger(Input(name="rsvp", party=new_member))

    rsvp_messages = {
        1: "Thank you for your RSVP! We're excited to have you on the team.",
        2: "We're sorry to hear that. Let us know if you change your mind!",
        3: "We'll keep a spot for you! Let us know your final decision soon."
    }

    for code, team_name in secret_team_codes.items():
        joined_team = (team_code_input == team_name).if_else(
            SecretInteger(welcome_messages[code]),
            joined_team
        )

    rsvp_status = rsvp_input.if_else(
        SecretInteger(rsvp_messages[1]),
        (rsvp_input == SecretInteger(2)).if_else(
            SecretInteger(rsvp_messages[2]),
            SecretInteger(rsvp_messages[3])
        )
    )

    final_message = joined_team + " " + rsvp_status

    out = Output(final_message, "joined_team", new_member)

    return [out]
