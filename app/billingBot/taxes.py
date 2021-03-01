
# List of states
CONTIGUOUS_STATES = (
    ('AL', "Alabama" , ('3.600')),
    ('AZ', "Arizona" , ('1.890')),
    ('AR', "Arkansas" , ('2.500')),
    ('CO', "Colorado" , ('2.000')),
    ('GA', "Georgia" , ('2.250')),
    ('IL', "Illinois" , ('3.500')),
    ('IN', "Indiana" , ('2.500')),
    ('MD', "Maryland" , ('2.000')),
    ('MN', "Minnesota" , ('2.000')),
    ('MS', "Mississippi" , ('3.000')),
    ('MO', "Missouri" , ('2.000')),
    ('NV', "Nevada" , ('3.500')),
    ('NM', "New Mexico" , ('3.003')),
    ('NC', "North Carolina" , ('2.640')),
    ('OH', "Ohio" , ('1.400')),
    ('PA', "Pennsylvania" , ('2.000')),
    ('SC', "South Carolina" , ('1.250')),
    ('TN', "Tennessee" , ('2.250')),
    ('TX', "Texas" , ('1.600')),
    ('UT', "Utah" , ('0.450')),
    ('WI', "Wisconsin" , ('2.000')),
)


def calculate_tax(state):
    """
        A function that take the state and return the tax.
        If the return value is 0, the State is not in the list.
        The function can take upper and lower case string and can ignore white spaces
    """
    tax = '0'
    for x in CONTIGUOUS_STATES:
        if (x[0] == state.upper().replace(" ", "") or
            x[1].upper().replace(" ", "") == state.upper().replace(" ", "")):

            tax = x[2]
    return tax

tax = calculate_tax('sC')