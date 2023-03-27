# exec
from apps.account.schemas import StateContract

# inspect the contract
props = StateContract.schema()["properties"]
for key in props:
    print(key, "prop is of type", props[key]["type"])

# create a contract
user_state_data = {
    "is_connected": True,
    "username": "johndoe",
}
state_contract = StateContract(**user_state_data)
print("The contract json payload:", str(state_contract.json(indent=2)))
