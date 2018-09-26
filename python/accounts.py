accounts = {"Emma": "emma"}
#function adds user details to accounts
def add_account(name, password):
    """
    Adds the key value pair to the accounts dictionary
    :param name:
    :param password:
    :return accounts:
    """
    accounts[name] = password
    return accounts


def login(name, password):
    """
    Returns true if the password and the corressponding name exist in the accounts dictionary
    :param name:
    :param password:
    :return
    """
    for key in accounts:
        if accounts[name] is password:
            return True
    
