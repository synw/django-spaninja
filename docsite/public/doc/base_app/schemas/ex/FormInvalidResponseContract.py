# exec
from django.contrib.auth.forms import UserCreationForm
from apps.base.schemas import FormInvalidResponseContract

# inspect the contract
props = FormInvalidResponseContract.schema()["properties"]
for key in props:
    print(key, "prop is of type", props[key]["type"])

# create a contract
data = {
    "username": "john",
    "password1": "foo",
    "password2": "bar",
}
form = UserCreationForm(data=data)
print("The Django form has errors:")
print(form.errors)
json_errs = form.errors.get_json_data(escape_html=True)
instance_contract = FormInvalidResponseContract(errors=json_errs)
str(instance_contract)
