# exec
from apps.base.schemas import MsgResponseContract

# inspect the contract
props = MsgResponseContract.schema()["properties"]
for key in props:
    print(key, "prop is of type", props[key]["type"])

# create a contract
instance = {
    "message": "A message",
}
instance_contract = MsgResponseContract(**instance)
print("The contract json payload:", str(instance_contract.json(indent=2)))
