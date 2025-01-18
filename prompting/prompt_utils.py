import textwrap

MULTISTEP_ARITHMETIC_PROMPTS = {
    "DIRECT_TEMPLATE" : (
        '{input} ?\n{steps}\nQ: Is there a mistake in this sequence? Write "No"'
        " if there are no mistakes, or the number N if there is a mistake in"
        " Thought N."
    ),
    
    "DIRECT_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "For each sequence of steps, identify the first mistake made, if"
                " any."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)) = ?
                Thought 1: This equation can be written as "(A + B) * (C * D)", where A = (-4 * -9 + -9 * 5) and B = (4 * 6 - -6 - 4) and C = (9 - 6 + -2 - 2) and D = (-2 * -5 - 6 * 7).
                Thought 2: Let's calculate A = (-4 * -9 + -9 * 5) = ((-4 * -9) + (-9 * 5)) = (36 + (-9 * 5)) = (36 + -45) = -9.
                Thought 3: Let's calculate B = (4 * 6 - -6 - 4) = ((4 * 6) - -6 - 4) = ((24) - -6 - 4) = ((24 - -6) - 4) = ((30) - 4) = 26.
                Thought 4: Let's calculate C = (9 - 6 + -2 - 2) = ((9 - 6) + -2 - 2) = ((3) + -2 - 2) = ((3 + -2) - 2) = ((1) - 2) = -1.
                Thought 5: Let's calculate D = (-2 * -5 - 6 * 7) = ((-2 * -5) - (6 * 7)) = ((10) - (6 * 7)) = (10 - (42)) = -32.
                Thought 6: Then, the final equation is (A + B) * (C * D) = (-9 + 26) * (-1 * -32) = (17) * (-1 * -32) = 17 * (32) = 544. So the answer is 544
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((((9 * 7 - -5 + 4) * (7 * -1 * -2 + 1)) - ((-4 - 6 + -6 * -8) * (5 + 7 - -6 - -7))) - (((-3 - -4 - -7 - 3) + (-3 * 4 - 3 + -5)) - ((7 - 2 - 2 - -7) + (5 + -1 - -3 * 7)))) = ?
                Thought 1: This equation can be written as "((A * B) - (C * D)) - ((E + F) - (G + H))", where A = (9 * 7 - -5 + 4) and B = (7 * -1 * -2 + 1) and C = (-4 - 6 + -6 * -8) and D = (5 + 7 - -6 - -7) and E = (-3 - -4 - -7 - 3) and F = (-3 * 4 - 3 + -5) and G = (7 - 2 - 2 - -7) and H = (5 + -1 - -3 * 7).
                Thought 2: Let's calculate A = (9 * 7 - -5 + 4) = ((9 * 7) - -5 + 4) = ((63) - -5 + 4) = ((63 - -5) + 4) = ((68) + 4) = 72.
                Thought 3: Let's calculate B = (7 * -1 * -2 + 1) = ((7 * -1 * -2) + 1) = ((-7) * -2 + 1) = ((-7 * -2) + 1) = ((14) + 1) = 15.
                Thought 4: Let's calculate C = (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
                Thought 5: Let's calculate D = (5 + 7 - -6 - -7) = ((5 + 7) - -6 - -7) = ((12) - -6 - -7) = ((12 - -6) - -7) = ((18) - -7) = 25.
                Thought 6: Let's calculate E = (-3 - -4 - -7 - 3) = ((-3 - -4) - -7 - 3) = ((1) - -7 - 3) = ((1 - -7) - 3) = ((8) - 3) = 5.
                Thought 7: Let's calculate F = (-3 * 4 - 3 + -5) = ((-3 * 4) - 3 + -5) = ((-12) - 3 + -5) = ((-12 - 3) + -5) = ((-15) + -5) = -20.
                Thought 8: Let's calculate G = (7 - 2 - 2 - -7) = ((7 - 2) - 2 - -7) = ((5) - 2 - -7) = ((5 - 2) - -7) = ((3) - -7) = 10.
                Thought 9: Let's calculate H = (5 + -1 - -3 * 7) = (5 + -1 - (-3 * 7)) = (5 + -1 - (-21)) = ((5 + -1) - -21) = ((4) - -21) = 25.
                Thought 10: Then, the final equation is ((A * B) - (C * D)) - ((E + F) - (G + H)) = ((72 * 15) - (128 * 25)) - ((5 + -20) - (10 + 25)) = ((1080) - (3200)) - ((-15) - (35)) = (-2120) - (-50) = -2070. So the answer is -2070
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "4"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((-3 + 5 * 8 * -4) - (9 - 8 * -7 + -9)) = ?
                Thought 1: This equation can be written as "A - B", where A = (-3 + 5 * 8 * -4) and B = (9 - 8 * -7 + -9).
                Thought 2: Let's calculate A = (-3 + 5 * 8 * -4) = (-3 + (5 * 8) * -4) = (-3 + (40) * -4) = (-3 + (40 * -4)) = (-3 + (-160)) = -163.
                Thought 3: Let's calculate B = (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
                Thought 4: Then, the final equation is A - B = -163 - 49 = -212. So the answer is -212
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "3"},
    ),
    
    "DIRECT_PERSTEP_TEMPLATE" : (
        '{input} ?\n{steps}\nQ: Is Thought {current_step} correct? Simply write "Yes" if'
        ' it is correct, and "No" if it is not. Do not need to explain or write anything else.'
    ),

    "DIRECT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                ' solving the math question. Write "Yes" if it is correct, and "No"'
                " if it is not."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)) = ?
                Thought 1: This equation can be written as "(A + B) * (C * D)", where A = (-4 * -9 + -9 * 5) and B = (4 * 6 - -6 - 4) and C = (9 - 6 + -2 - 2) and D = (-2 * -5 - 6 * 7).
                Q: Is Thought 1 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "Yes"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((((9 * 7 - -5 + 4) * (7 * -1 * -2 + 1)) - ((-4 - 6 + -6 * -8) * (5 + 7 - -6 - -7))) - (((-3 - -4 - -7 - 3) + (-3 * 4 - 3 + -5)) - ((7 - 2 - 2 - -7) + (5 + -1 - -3 * 7)))) = ?
                Thought 1: This equation can be written as "((A * B) - (C * D)) - ((E + F) - (G + H))", where A = (9 * 7 - -5 + 4) and B = (7 * -1 * -2 + 1) and C = (-4 - 6 + -6 * -8) and D = (5 + 7 - -6 - -7) and E = (-3 - -4 - -7 - 3) and F = (-3 * 4 - 3 + -5) and G = (7 - 2 - 2 - -7) and H = (5 + -1 - -3 * 7).
                Thought 2: Let's calculate A = (9 * 7 - -5 + 4) = ((9 * 7) - -5 + 4) = ((63) - -5 + 4) = ((63 - -5) + 4) = ((68) + 4) = 72.
                Thought 3: Let's calculate B = (7 * -1 * -2 + 1) = ((7 * -1 * -2) + 1) = ((-7) * -2 + 1) = ((-7 * -2) + 1) = ((14) + 1) = 15.
                Thought 4: Let's calculate C = (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
                Q: Is Thought 4 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((-3 + 5 * 8 * -4) - (9 - 8 * -7 + -9)) = ?
                Thought 1: This equation can be written as "A - B", where A = (-3 + 5 * 8 * -4) and B = (9 - 8 * -7 + -9).
                Thought 2: Let's calculate A = (-3 + 5 * 8 * -4) = (-3 + (5 * 8) * -4) = (-3 + (40) * -4) = (-3 + (40 * -4)) = (-3 + (-160)) = -163.
                Thought 3: Let's calculate B = (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
                Q: Is Thought 3 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "No"},
    ),


    "COT_PERSTEP_TEMPLATE" : (
        "{input} ?\n{steps}\nQ:"
        " Is Thought {current_step} correct? Check through"
        " each equation and determine whether there are any errors."
    ),

    "COT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                " solving the math question. End your response with Yes if the"
                " thought is correct, No if the thought is incorrect."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)) = ?
                Thought 1: This equation can be written as "(A + B) * (C * D)", where A = (-4 * -9 + -9 * 5) and B = (4 * 6 - -6 - 4) and C = (9 - 6 + -2 - 2) and D = (-2 * -5 - 6 * 7).
                Q: Is Thought 1 correct? Check through each equation and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 1 by checking each equation. Thought 1 rewrites the original equation as (A + B) * (C * D). I can check if this is correct by replacing each letter with the corresponding equation, and checking the final result against the original equation. Current equation: (A + B) * (C * D)
                Comment 2: Replacing A: According to Thought 1, A is (-4 * -9 + -9 * 5). The current equation is (A + B) * (C * D), so after the replacement: ((-4 * -9 + -9 * 5) + B) * (C * D).
                Comment 3: Replacing B: According to Thought 1, B is (4 * 6 - -6 - 4). The current equation is ((-4 * -9 + -9 * 5) + B) * (C * D), so after the replacement: ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * (C * D)
                Comment 4: Replacing C: According to Thought 1, C is (9 - 6 + -2 - 2). The current equation is ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * (C * D), so after the replacement: ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * D)
                Comment 5: Replacing D: According to Thought 1, D is (-2 * -5 - 6 * 7). The currnet equation is ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * D), so after the replacement: ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7))
                Comment 6: The final equation is ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)). The original equation was ((-4 * -9 + -9 * 5) + (4 * 6 - -6 - 4)) * ((9 - 6 + -2 - 2) * (-2 * -5 - 6 * 7)). So Thought 1 is correct. Yes"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((((9 * 7 - -5 + 4) * (7 * -1 * -2 + 1)) - ((-4 - 6 + -6 * -8) * (5 + 7 - -6 - -7))) - (((-3 - -4 - -7 - 3) + (-3 * 4 - 3 + -5)) - ((7 - 2 - 2 - -7) + (5 + -1 - -3 * 7)))) = ?
                Thought 1: This equation can be written as "((A * B) - (C * D)) - ((E + F) - (G + H))", where A = (9 * 7 - -5 + 4) and B = (7 * -1 * -2 + 1) and C = (-4 - 6 + -6 * -8) and D = (5 + 7 - -6 - -7) and E = (-3 - -4 - -7 - 3) and F = (-3 * 4 - 3 + -5) and G = (7 - 2 - 2 - -7) and H = (5 + -1 - -3 * 7).
                Thought 2: Let's calculate A = (9 * 7 - -5 + 4) = ((9 * 7) - -5 + 4) = ((63) - -5 + 4) = ((63 - -5) + 4) = ((68) + 4) = 72.
                Thought 3: Let's calculate B = (7 * -1 * -2 + 1) = ((7 * -1 * -2) + 1) = ((-7) * -2 + 1) = ((-7 * -2) + 1) = ((14) + 1) = 15.
                Thought 4: Let's calculate C = (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
                Q: Is Thought 4 correct? Check through each equation and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 4 by checking each equation. The order of operations in mathematics is parentheses, exponents, multiplication and division, addition and subtraction, so I need to ensure that the equations follow this order. Remaining: C = (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
                Comment 2: Checking: C = (-4 - 6 + -6 * -8). According to Thought 1, C is (9 - 6 + -2 - 2). So C = (-4 - 6 + -6 * -8) is correct. Remaining: (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) = ((-10) + -6 * -8) = ((-10 + -6) * -8) = ((-16) * -8) = 128.
                Comment 3: Checking: (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8). So the first operation in (-4 - 6 + -6 * -8) should be the multiplication -6 * -8. The equation (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) places parentheses around the subtraction -4 - 6, which is incorrect.
                Comment 4: (-4 - 6 + -6 * -8) = ((-4 - 6) + -6 * -8) is incorrect. So Thought 4 is incorrect. No"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                ((-3 + 5 * 8 * -4) - (9 - 8 * -7 + -9)) = ?
                Thought 1: This equation can be written as "A - B", where A = (-3 + 5 * 8 * -4) and B = (9 - 8 * -7 + -9).
                Thought 2: Let's calculate A = (-3 + 5 * 8 * -4) = (-3 + (5 * 8) * -4) = (-3 + (40) * -4) = (-3 + (40 * -4)) = (-3 + (-160)) = -163.
                Thought 3: Let's calculate B = (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 56.
                Q: Is Thought 3 correct? Check through each equation and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 7 by checking each equation. The order of operations in mathematics is parentheses, exponents, multiplication and division, addition and subtraction, so I need to ensure that the equations follow this order. Remaining: B = (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
                Comment 2: Checking: B = (9 - 8 * -7 + -9). According to Thought 1, B is (9 - 8 * -7 + -9). So B = (9 - 8 * -7 + -9) is correct. Remaining: (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
                Comment 3: Checking: (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9). The first operation in (9 - 8 * -7 + -9) should be the multiplication 8 * -7. The equation (9 - 8 * -7 + -9) = (9 - (8 * -7) + -9) places parentheses around the multiplication 8 * -7, which is correct. Remaining: (9 - (8 * -7) + -9) = (9 - (-49) + -9) = ((9 - -49) + -9) = ((58) + -9) = 49.
                Comment 4: Checking: (9 - (8 * -7) + -9) = (9 - (-49) + -9). The first operation in (9 - (8 * -7) + -9) should be the parentheses (8 * -7), which equals -56. The equation (9 - (8 * -7) + -9) = (9 - (-49) + -9) replaces 8 * -7 with -49, which is incorrect.
                Comment 5: (9 - (8 * -7) + -9) = (9 - (-49) + -9) is incorrect. So Thought 7 is incorrect. No"""
            ),
        },
    )
}

DYCK_LANGUAGES_PROMPTS = {
    "DIRECT_TEMPLATE" : (
        "Task: Complete the rest of the sequence, making sure that the parentheses"
        " are closed properly. Input: {input}\n{steps}\nQ: Is there a mistake in"
        ' this sequence? Write "No" if there are no mistakes, or the number N if'
        " there is a mistake in Thought N."
    ),

    "DIRECT_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "For each sequence of steps, identify the first mistake made, if"
                " any."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: [ { [
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: [ ; stack: [
                Thought 4: { ; stack: [ {
                Thought 5: [ ; stack: [ { [
                Thought 6: Now, we have reached the end. The final stack is "[ { [".
                Thought 7: We will need to pop out "[", "{", one by one in that order.
                Thought 8: So, we need "]", "}". So the answer is ] }
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "7"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < > ( ( [ [ ( { } ) [ < > ] ]
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: < ; stack: <
                Thought 4: > ; stack: empty
                Thought 5: ( ; stack: (
                Thought 6: ( ; stack: ( (
                Thought 7: [ ; stack: ( ( [
                Thought 8: [ ; stack: ( ( [ [
                Thought 9: ( ; stack: ( ( [ [ (
                Thought 10: { ; stack: ( ( [ [ ( {
                Thought 11: } ; stack: ( ( [ [ (
                Thought 12: ) ; stack: ( ( [ [
                Thought 13: [ ; stack: ( ( [ [ [
                Thought 14: < ; stack: ( ( [ [ [ <
                Thought 15: > ; stack: ( ( [ [ [
                Thought 16: ] ; stack: ( ( [ [
                Thought 17: ] ; stack: ( ( [
                Thought 18: Now, we have reached the end. The final stack is "( ( [".
                Thought 19: We will need to pop out "[", "(", "(" one by one in that order.
                Thought 20: So, we need "]", ")", ")". So the answer is ] ) )
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < [ < [ { < [ ] < { } > > } ] > { { ( ) } { < [ < > ] > }
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: < ; stack: <
                Thought 4: [ ; stack: < [
                Thought 5: < ; stack: < [ <
                Thought 6: [ ; stack: < [ < [
                Thought 7: { ; stack: < [ < [ {
                Thought 8: < ; stack: < [ < [ { <
                Thought 9: [ ; stack: < [ < [ { < [
                Thought 10: ] ; stack: < [ < [ { <
                Thought 11: < ; stack: < [ < [ { < <
                Thought 12: { ; stack: < [ < [ { < < {
                Thought 13: } ; stack: < [ < [ { < <
                Thought 14: > ; stack: < [ < [ { <
                Thought 15: > ; stack: < [ < [ {
                Thought 16: } ; stack: < [ < [
                Thought 17: ] ; stack: < [ <
                Thought 18: > ; stack: < [
                Thought 19: Now, we have reached the end. The final stack is "< [".
                Thought 20: We will need to pop out "[", "<" one by one in that order.
                Thought 21: So, we need "]", ">". So the answer is } >
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "19"},
    ),


    "DIRECT_PERSTEP_TEMPLATE" : (
        "Task: Complete the rest of the sequence, making sure that the brackets"
        " are closed properly. Input: {input}\n{steps}\nQ: Is Thought"
        ' {current_step} correct? Write "Yes" if it is correct, and "No" if it is'
        " not. Do not need to explain."
    ),


    "DIRECT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                " solving the question. Write \"Yes\" if the"
                " thought is correct, \"No\" if the thought is incorrect."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: [ {
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: [ ; stack: [
                Thought 4: { ; stack: [ {
                Thought 5: Now, we have reached the end. The final stack is "[ {".
                Thought 6: We will need to pop out "{", "[" one by one in that order.
                Thought 7: So, we need "{", "[". So the answer is { [
                Q: Is Thought 7 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {
            "role": "assistant",
            "content": "No",
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the brackets are closed properly. Input: < > ( ( [ [ ( { } ) [ < > ] ]
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: < ; stack: <
                Thought 4: > ; stack: empty
                Q: Is Thought 4 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {
            "role": "assistant",
            "content": "Yes"
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < [ < [ { < [ ] < { } > > } ] > { { ( ) } { < [ < > ] > }
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: < ; stack: <
                Thought 4: [ ; stack: < [
                Thought 5: < ; stack: < [ <
                Thought 6: [ ; stack: < [ < [
                Thought 7: { ; stack: < [ <
                Q: Is Thought 7 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {
            "role": "assistant",
            "content": "No"
        },
    ),

    "COT_PERSTEP_TEMPLATE" : (
        "Task: Complete the rest of the sequence, making sure that the brackets"
        " are closed properly. Input: {input}\n{steps}\nQ:"
        " Is Thought {current_step} correct? Check through"
        " each sentence and determine whether there are any errors."
    ),

    "COT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                " solving the question. End your response with Yes if the"
                " thought is correct, No if the thought is incorrect."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: [ {
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: [ ; stack: [
                Thought 4: { ; stack: [ {
                Thought 5: Now, we have reached the end. The final stack is "[ {".
                Thought 6: We will need to pop out "{", "[" one by one in that order.
                Thought 7: So, we need "{", "[". So the answer is { [
                Q: Is Thought 7 correct? Check through each sentence and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 7 by checking each sentence. Remaining: So, we need "{", "[". So the answer is { [
                Comment 2: Checking: So, we need "[", "{", "[". Thought 6 states that we need to pop out "{", "[", so we need to find the sequence of matching bracket pairs. So we need "}", "]". This does not match the part we are checking. So So we need "}", "]" is incorrect.
                Comment 3: So we need "}", "]" is incorrect, so Thought 6 is incorrect. No"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the brackets are closed properly. Input: < > ( ( [ [ ( { } ) [ < > ] ]
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: < ; stack: <
                Thought 4: > ; stack: empty
                Q: Is Thought 4 correct? Check through each sentence and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 4 by checking each sentence. Remaining: > ; stack: empty
                Comment 2: Checking: >. Thought 4 should look at the 2nd symbol in the input, >. This matches the symbol we are checking, >. So > is correct. Remaining: stack: empty
                Comment 3: Checking: stack: empty. Thought 4 should check if the second symbol > forms a bracket pair with the top item on the stack in Thought 3. If it does, the top item should be removed; if it does not, the new symbol should be added to the top of the stack. The stack in Thought 4 is <. After processing the symbol >, the stack should be empty. So stack: empty is correct. Remaining:
                Comment 4: > ; stack: empty is correct, so Thought 5 is correct. Yes"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < [ < [ { < [ ] < { } > > } ] > { { ( ) } { < [ < > ] > }
                Thought 1: We should process each input one by one and keep track of the stack configuration.
                Thought 2: stack: empty
                Thought 3: < ; stack: <
                Thought 4: [ ; stack: < [
                Thought 5: < ; stack: < [ <
                Thought 6: [ ; stack: < [ < [
                Thought 7: { ; stack: < [ <
                Q: Is Thought 7 correct? Check through each sentence and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 7 by checking each sentence. Remaining: { ; stack: < [ <
                Comment 2: Checking: {. Thought 7 should look at the 5th symbol in the input, {. This matches the symbol we are checking, {. So { is correct. Remaining: stack: < [ <
                Comment 3: Checking: stack: < [ <. Thought 7 should check if the 5th symbol { forms a bracket pair with the top item on the stack in Thought 6. If it does, the top item should be removed; if it does not, the new symbol should be added to the top of the stack. The stack in Thought 6 is < [ < [. After processing the symbol {, the stack should be < [ < [ {. So stack: < [ < is incorrect. Remaining:
                Comment 4: stack: < [ < is incorrect, so Thought 7 is incorrect. No"""
            ),
        },
    )
}

LOGICAL_DEDUCTION_PROMPTS = {
    "DIRECT_TEMPLATE" : (
        '{input}\n{steps}\nQ: Is there a mistake in this sequence? Write "No"'
        " if there are no mistakes, or the number N if there is a mistake in"
        " Thought N."
    ),

    "DIRECT_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "For each sequence of steps, identify the first mistake made, if"
                " any."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of five objects arranged in a fixed order. The statements are logically consistent.
                - In a golf tournament, there were five golfers: Amy, Eli, Eve, Bob, and Avery.
                - Eve finished above Bob.
                - Eli finished third.
                - Amy finished below Avery.
                - Avery finished second to last.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) Amy finished first
                (B) Eli finished first
                (C) Eve finished first
                (D) Bob finished first
                (E) Avery finished first
                Thought 1: To answer the question, I need to identify the positions of all five golfers. I should first find and look through any statements about absolute positions of golfers. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: Eli finished third. There are five golfers in total, so Eli is in the middle.
                Thought 3: So from first to last: first and second can be any golfer, then third is Eli, then fourth is Avery, then fifth can be any golfer.
                Thought 4: Amy finished below Avery. Previously, we concluded that Avery is fourth and there are only a total of 5 golfers, so Amy must be fifth.
                Thought 5: So from first to last: first and second can be any golfer, then third is Eli, then fourth is Avery, then fifth is Amy.
                Thought 6: Eve finished above Bob. Previously, we concluded that first and second are the only unknown golfers, so they must be Eve and Bob. Since Eve finished above Bob. Eve must be first, and Bob must be second.
                Thought 7: So from first to last: first is Eve, then second is Bob, then third is Eli, then fourth is Avery, then fifth is Amy.
                Thought 10: According to this ordering, the person who finished first is Eve. So the answer is (C)
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "3"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of three objects arranged in a fixed order. The statements are logically consistent.
                - On a shelf, there are three books: a white book, a green book, and an orange book.
                - The green book is to the right of the white book.
                - The orange book is to the right of the green book.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) The white book is the leftmost
                (B) The green book is the leftmost
                (C) The orange book is the leftmost
                Thought 1: To answer the question, I need to identify the positions of all three books. I should first find and look through any statements about absolute positions of books. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: The green book is to the right of the white book, so the green book cannot be the leftmost and the white book cannot be the rightmost.
                Thought 3: So from left to right: first is the white book or the orange book, then second can be any book, then third is the green book or the orange book.
                Thought 4: The orange book is to the right of the green book, so the orange book cannot be the leftmost. We previously concluded that the leftmost book is the white book or the orange book, so the leftmost book must be the white book.
                Thought 5: The orange book is to the right of the green book, so the green book cannot be the rightmost. We previously concluded that the rightmost book is the green book or the orange book, so the rightmost book must be the orange book.
                Thought 6: By process of elimination, the middle book must be the green book.
                Thought 7: So from left to right: first is the white book, then second is the green book, then third is the orange book. 
                Thought 8: According to this ordering, the leftmost book is the white book. So the answer is (A)
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of five objects arranged in a fixed order. The statements are logically consistent.
                - On a shelf, there are five books: a red book, a gray book, a white book, a blue book, and a green book.
                - The white book is to the left of the gray book.
                - The gray book is the third from the left.
                - The red book is the second from the left.
                - The blue book is to the right of the green book.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) The red book is the leftmost
                (B) The gray book is the leftmost
                (C) The white book is the leftmost
                (D) The blue book is the leftmost
                (E) The green book is the leftmost
                Thought 1: To answer the question, I need to identify the positions of all five books. I should first find and look through any statements about absolute positions of books. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: The gray book is third from the left. So from left to right: first and second can be any book, then third is the gray book, then fourth and fifth can be any book.
                Thought 3: The white book is to the left of the gray book. We previously concluded that the gray book is third from the left, so the white book must be second from the left.
                Thought 4: So from left to right: first can be any book, then second is the white book, then third is the gray book, then fourth and fifth can be any book.
                Thought 5: The red book is second from the left. So from left to right: first is the white book, then second is the red book, then third is the gray book, then fourth and fifth can be any book.
                Thought 6: The blue book is to the right of the green book. Previously, we concluded that fourth and fifth are the only unknown books, so they must be blue and green. Since the blue book is to the right of the green book, the blue book must be fourth and the green book must be fifth.
                Thought 7: So from left to right: first is the white book, then second is the red book, then third is the gray book, then fourth is the blue book, then fifth is the green book.
                Thought 8: According to this ordering, the leftmost book is the white book. So the answer is (C)
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "3"},
    ),


    "DIRECT_PERSTEP_TEMPLATE" : (
        '{input}\n{steps}\n\nIs Thought {current_step} correct? Write "Yes" if it'
        ' is correct, and "No" if it is not. Do not need to explain.'
    ),

    "DIRECT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                ' solving the question. Write "Yes" if it is correct, and "No" if'
                " it is not."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of five objects arranged in a fixed order. The statements are logically consistent.
                - In a golf tournament, there were five golfers: Amy, Eli, Eve, Bob, and Avery.
                - Eve finished above Bob.
                - Eli finished third.
                - Amy finished below Avery.
                - Avery finished second to last.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) Amy finished first
                (B) Eli finished first
                (C) Eve finished first
                (D) Bob finished first
                (E) Avery finished first
                Thought 1: To answer the question, I need to identify the positions of all five golfers. I should first find and look through any statements about absolute positions of golfers. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: Eli finished third. There are five golfers in total, so Eli is in the middle.
                Thought 3: So from first to last: first and second can be any golfer, then third is Eli, then fourth is Avery, then fifth can be any golfer.
                
                Is Thought 3 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of three objects arranged in a fixed order. The statements are logically consistent.
                - On a shelf, there are three books: a white book, a green book, and an orange book.
                - The green book is to the right of the white book.
                - The orange book is to the right of the green book.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) The white book is the leftmost
                (B) The green book is the leftmost
                (C) The orange book is the leftmost
                Thought 1: To answer the question, I need to identify the positions of all three books. I should first find and look through any statements about absolute positions of books. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: The green book is to the right of the white book, so the green book cannot be the leftmost and the white book cannot be the rightmost.
                Thought 3: So from left to right: first is the white book or the orange book, then second can be any book, then third is the green book or the orange book.
                Thought 4: The orange book is to the right of the green book, so the orange book cannot be the leftmost. We previously concluded that the leftmost book is the white book or the orange book, so the leftmost book must be the white book.
                
                Is Thought 4 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "Yes"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of five objects arranged in a fixed order. The statements are logically consistent.
                - On a shelf, there are five books: a red book, a gray book, a white book, a blue book, and a green book.
                - The white book is to the left of the gray book.
                - The gray book is the third from the left.
                - The red book is the second from the left.
                - The blue book is to the right of the green book.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) The red book is the leftmost
                (B) The gray book is the leftmost
                (C) The white book is the leftmost
                (D) The blue book is the leftmost
                (E) The green book is the leftmost
                Thought 1: To answer the question, I need to identify the positions of all five books. I should first find and look through any statements about absolute positions of books. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: The gray book is third from the left. So from left to right: first and second can be any book, then third is the gray book, then fourth and fifth can be any book.
                Thought 3: The white book is to the left of the gray book. We previously concluded that the gray book is third from the left, so the white book must be second from the left.
                
                Is Thought 3 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "No"},
    ),

    "COT_PERSTEP_TEMPLATE" : (
        "{input}\n{steps}\n\nIs Thought {current_step} correct? Check through"
        " each part of the text and determine whether there are any errors."
    ),

    "COT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                " solving the question. End your response with Yes if the"
                " thought is correct, No if the thought is incorrect."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of five objects arranged in a fixed order. The statements are logically consistent.
                - In a golf tournament, there were five golfers: Amy, Eli, Eve, Bob, and Avery.
                - Eve finished above Bob.
                - Eli finished third.
                - Amy finished below Avery.
                - Avery finished second to last.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) Amy finished first
                (B) Eli finished first
                (C) Eve finished first
                (D) Bob finished first
                (E) Avery finished first
                Thought 1: To answer the question, I need to identify the positions of all five golfers. I should first find and look through any statements about absolute positions of golfers. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: Eli finished third. There are five golfers in total, so Eli is in the middle.
                Thought 3: So from first to last: first and second can be any golfer, then third is Eli, then fourth is Avery, then fifth can be any golfer.
                
                Is Thought 3 correct? Check through each part of the text and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 3 by checking through each part of the text. Previous Thoughts have concluded the following information: Eli finished third (Thought 2). Remaining: So from first to last: first and second can be any golfer, then third is Eli, then fourth is Avery, then fifth can be any golfer.
                Comment 2: Checking: So from first to last: first and second can be any golfer. According to the information in previous Thoughts, currently there is no information about the first and second golfer. So "So from first to last: first and second can be any golfer" is correct. Remaining: Then third is Eli, then fourth is Avery, then fifth can be any golfer.
                Comment 3: Checking: Then third is Eli. According to the information in previous Thoughts, Eli finished third (Thought 2). So "Then third is Eli" is correct. Remaining: Then fourth is Avery, then fifth can be any golfer.
                Comment 4: Checking: Then fourth is Avery. According to the information in previous Thoughts, currently there is no information about the fourth folger. So "Then fourth is Avery" is incorrect.
                Comment 5: "Then fourth is Avery" is incorrect. So Thought 3 is incorrect. No"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of three objects arranged in a fixed order. The statements are logically consistent.
                - On a shelf, there are three books: a white book, a green book, and an orange book.
                - The green book is to the right of the white book.
                - The orange book is to the right of the green book.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) The white book is the leftmost
                (B) The green book is the leftmost
                (C) The orange book is the leftmost
                Thought 1: To answer the question, I need to identify the positions of all three books. I should first find and look through any statements about absolute positions of books. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: The green book is to the right of the white book, so the green book cannot be the leftmost and the white book cannot be the rightmost.
                Thought 3: So from left to right: first is the white book or the orange book, then second can be any book, then third is the green book or the orange book.
                Thought 4: The orange book is to the right of the green book, so the orange book cannot be the leftmost. We previously concluded that the leftmost book is the white book or the orange book, so the leftmost book must be the white book.
                
                Is Thought 4 correct? Check through each part of the text and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 4 by checking through each part of the text. Previous Thoughts have concluded the following information: The green book is to the right of the white book (Thought 2); The green book cannot be leftmost (Thought 2); The white book cannot be rightmost (Thought 2). Remaining: The orange book is to the right of the green book, so the orange book cannot be the leftmost. We previously concluded that the leftmost book is the white book or the orange book, so the leftmost book must be the white book.
                Comment 2: Checking: The orange book is to the right of the green book. In the original question, the statement "The orange book is to the right of the green book" can be found. So "The orange book is to the right of the green book" is correct. Remaining: So the orange book cannot be the leftmost. We previously concluded that the leftmost book is the white book or the orange book, so the leftmost book must be the white book.
                Comment 3: Checking: So the orange book cannot be the leftmost. Since the orange book is to the right of the green book, therefore the green book is to the left of the orange book. If the orange book is leftmost, the green book cannot be placed. So "So the orange book cannot be the leftmost" is correct. Remaining: We previously concluded that the leftmost book is the white book or the orange book, so the leftmost book must be the white book.
                Comment 4: Checking: We previously concluded that the leftmost book is the white book or the orange book. According to Thought 3, from left to right, the first is the white book or the orange book. So "We previously concluded that the leftmost book is the white book or the orange book" is correct. Remaining: So the leftmost book must be the white book.
                Comment 5: Checking: So the leftmost book must be the white book. According to Thought 3, we know that the leftmost book is the white book or the orange book. Since the orange book cannot be leftmost, the leftmost book can only be the white book. So "So the leftmost book must be the white book" is correct. Remaining:
                Comment 6: I have checked through all parts of the text and found no errors. So Thought 4 is correct. Yes"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                The following statements each describe a set of five objects arranged in a fixed order. The statements are logically consistent.
                - On a shelf, there are five books: a red book, a gray book, a white book, a blue book, and a green book.
                - The white book is to the left of the gray book.
                - The gray book is the third from the left.
                - The red book is the second from the left.
                - The blue book is to the right of the green book.
                Q: Given the above statements, which of the following is correct?
                Options:
                (A) The red book is the leftmost
                (B) The gray book is the leftmost
                (C) The white book is the leftmost
                (D) The blue book is the leftmost
                (E) The green book is the leftmost
                Thought 1: To answer the question, I need to identify the positions of all five books. I should first find and look through any statements about absolute positions of books. Then, if there are remaining gaps, I can look through statements about relative positions and find the final order by process of elimination.
                Thought 2: The gray book is third from the left. So from left to right: first and second can be any book, then third is the gray book, then fourth and fifth can be any book.
                Thought 3: The white book is to the left of the gray book. We previously concluded that the gray book is third from the left, so the white book must be second from the left.
                
                Is Thought 3 correct? Check through each part of the text and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 5 by checking through each part of the text. Previous Thoughts have concluded the following information: The gray book is third from the left (Thought 2). Remaining: The white book is to the left of the gray book. We previously concluded that the gray book is third from the left, so the white book must be second from the left.
                Comment 2: Checking: The white book is to the left of the gray book. In the original question, the statement "The white book is to the left of the gray book" can be found. So "The white book is to the left of the gray book" is correct. Remaining: We previously concluded that the gray book is third from the left, so the white book must be second from the left.
                Comment 3: Checking: We previously concluded that the gray book is third from the left. According to the information in previous Thoughts, we know that the gray book is third from the left (Thought 2). So "We previously concluded that the gray book is third from the left" is correct. Remaining: So the white book must be second from the left.
                Comment 4: Checking: So the white book must be second from the left.According to the information in previous Thoughts, we know that the gray book is third from the left (Thought 2), so the white book can be second from the left or leftmost. There are two possible options for the position of the white book, so "So the white book must be second from the left" is incorrect.
                Comment 5: "So the white book must be second from the left" is incorrect. So Thought 3 is incorrect. No"""
            ),
        },
    )
}

TRACKING_SHUFFLED_OBJECTS_PROMPTS = {
    "DIRECT_TEMPLATE" : (
        '{input}\n{steps}\nQ: Is there a mistake in this sequence? Write "No"'
        " if there are no mistakes, or the number N if there is a mistake in"
        " Thought N."
    ),

    "DIRECT_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "For each sequence of steps, identify the first mistake made, if"
                " any."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a yellow ball, Bob has a blue ball, and Claire has a pink ball.
                As the game progresses, pairs of players trade balls. First, Claire and Alice swap balls. Then, Alice and Bob swap balls. Finally, Claire and Bob swap balls. At the end of the game, Bob has the
                Options:
                (A) yellow ball
                (B) blue ball
                (C) pink ball
                Thought 1: At the start: Alice: yellow, Bob: blue, Claire: pink.
                Thought 2: Claire and Alice swap balls: Alice: pink, Bob: blue, Claire: yellow.
                Thought 3: Alice and Bob swap balls: Alice: yellow, Bob: blue, Claire: pink.
                Thought 4: Claire and Bob swap balls: Alice: yellow, Bob: pink, Claire: blue.
                Thought 5: At the end of the game, Bob has the pink ball. So the answer is (C)
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "3"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a white ball, Bob has a purple ball, and Claire has a pink ball.
                As the game progresses, pairs of players trade balls. First, Bob and Alice swap balls. Then, Bob and Claire swap balls. Finally, Bob and Alice swap balls. At the end of the game, Alice has the
                Options:
                (A) white ball
                (B) purple ball
                (C) pink ball
                Thought 1: At the start: Alice: white, Bob: purple, Claire: pink.
                Thought 2: Bob and Alice swap balls: Alice: purple, Bob: white, Claire: pink.
                Thought 3: Bob and Claire swap balls: Alice: purple, Bob: pink, Claire: white.
                Thought 4: Bob and Alice swap balls: Alice: pink, Bob: purple, Claire: white.
                Thought 5: At the end of the game, Alice has the pink ball. So the answer is (C)
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Lola, Bob is dancing with Rodrigo, and Claire is dancing with Patrick.
                Throughout the song, the dancers often trade partners. First, Alice and Bob switch partners. Then, Claire and Bob switch partners. Finally, Bob and Alice switch partners. At the end of the dance, Alice is dancing with
                Options:
                (A) Lola
                (B) Rodrigo
                (C) Patrick
                Thought 1: At the start: Alice: Lola, Bob: Rodrigo, Claire: Patrick.
                Thought 2: Alice and Bob switch partners: Alice: Rodrigo, Bob: Lola, Claire: Patrick.
                Thought 3: Claire and Bob switch partners: Alice: Rodrigo, Bob: Patrick, Claire: Lola.
                Thought 4: Alice and Claire switch partners: Alice: Lola, Bob: Patrick, Claire: Rodrigo.
                Thought 5: At the end of the dance, Alice is dancing with Lola. So the answer is (A)
                Q: Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "4"},
    ),


    "DIRECT_PERSTEP_TEMPLATE" : (
        '{input}\n{steps}\nQ: Is Thought {current_step} correct? Write "Yes" if it'
        ' is correct, and "No" if it is not. Do not need to explain.'
    ),

    "DIRECT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                ' solving the question. Write "Yes" if it is correct, and "No" if'
                " it is not."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a yellow ball, Bob has a blue ball, and Claire has a pink ball.
                As the game progresses, pairs of players trade balls. First, Claire and Alice swap balls. Then, Alice and Bob swap balls. Finally, Claire and Bob swap balls. At the end of the game, Bob has the
                Options:
                (A) yellow ball
                (B) blue ball
                (C) pink ball
                Thought 1: At the start: Alice: yellow, Bob: blue, Claire: pink.
                Thought 2: Claire and Alice swap balls: Alice: pink, Bob: blue, Claire: yellow.
                Thought 3: Alice and Bob swap balls: Alice: yellow, Bob: blue, Claire: pink.
                Q: Is Thought 3 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a white ball, Bob has a purple ball, and Claire has a pink ball.
                As the game progresses, pairs of players trade balls. First, Bob and Alice swap balls. Then, Bob and Claire swap balls. Finally, Bob and Alice swap balls. At the end of the game, Alice has the
                Options:
                (A) white ball
                (B) purple ball
                (C) pink ball
                Thought 1: At the start: Alice: white, Bob: purple, Claire: pink.
                Q: Is Thought 1 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "Yes"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Lola, Bob is dancing with Rodrigo, and Claire is dancing with Patrick.
                Throughout the song, the dancers often trade partners. First, Alice and Bob switch partners. Then, Claire and Bob switch partners. Finally, Bob and Alice switch partners. At the end of the dance, Alice is dancing with
                Options:
                (A) Lola
                (B) Rodrigo
                (C) Patrick
                Thought 1: At the start: Alice: Lola, Bob: Rodrigo, Claire: Patrick.
                Thought 2: Alice and Bob switch partners: Alice: Rodrigo, Bob: Lola, Claire: Patrick.
                Thought 3: Claire and Bob switch partners: Alice: Rodrigo, Bob: Patrick, Claire: Lola.
                Thought 4: Bob and Alice switch partners: Alice: Patrick, Bob: Rodrigo, Claire: Lola.
                Thought 5: At the end of the dance, Alice is dancing with Rodrigo. So the answer is (B)
                Q: Is Thought 5 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "No"},
    ),


    "COT_PERSTEP_TEMPLATE" : (
        "{input}\n{steps}\n\nIs Thought {current_step} correct? Check through"
        " each part of the text and determine whether there are any errors."
    ),

    "COT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                " solving the question. End your response with Yes if the"
                " thought is correct, No if the thought is incorrect."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a yellow ball, Bob has a blue ball, and Claire has a pink ball.
                As the game progresses, pairs of players trade balls. First, Claire and Alice swap balls. Then, Alice and Bob swap balls. Finally, Claire and Bob swap balls. At the end of the game, Bob has the
                Options:
                (A) yellow ball
                (B) blue ball
                (C) pink ball
                Thought 1: At the start: Alice: yellow, Bob: blue, Claire: pink.
                Thought 2: Claire and Alice swap balls: Alice: pink, Bob: blue, Claire: yellow.
                Thought 3: Alice and Bob swap balls: Alice: yellow, Bob: blue, Claire: pink.
                
                Is Thought 3 correct? Check through each part of the text and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 3 by checking through each part of the text. Remaining: Alice and Bob swap balls: Alice: yellow, Bob: blue, Claire: pink.
                Comment 2: Checking: Alice and Bob swap balls. This is the second swap in the sequence, after the swap between Claire and Alice. This matches the description in the original question. So Alice and Bob swap balls is correct. Remaining: Alice: yellow, Bob: blue, Claire: pink.
                Comment 3: Checking: Alice: yellow. In Thought 2, Alice had a pink ball and Bob had a blue ball. If Alice and Bob swapped balls, Alice should have a blue ball and Bob should have a pink ball. So Alice: yellow is incorrect.
                Comment 4: Alice: yellow is incorrect. So Thought 3 is incorrect. No"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a white ball, Bob has a purple ball, and Claire has a pink ball.
                As the game progresses, pairs of players trade balls. First, Bob and Alice swap balls. Then, Bob and Claire swap balls. Finally, Bob and Alice swap balls. At the end of the game, Alice has the
                Options:
                (A) white ball
                (B) purple ball
                (C) pink ball
                Thought 1: At the start: Alice: white, Bob: purple, Claire: pink.
                
                Is Thought 1 correct? Check through each part of the text and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 1 by checking through each part of the text. Remaining: At the start: Alice: white, Bob: purple, Claire: pink.
                Comment 2: Checking: At the start. This is the first thought in the sequence, so this is correct. Remaining: Alice: white, Bob: purple, Claire: pink.
                Comment 3: Checking: Alice: white. In the description of the original question, at the start of the game, Alice has a white ball. So Alice: white is correct. Remaining: Bob: purple, Claire: pink.
                Comment 4: Checking: Bob: purple. In the description of the original question, at the start of the game, Bob has a purple ball. So Bob: purple is correct. Remaining: Claire: pink.
                Comment 5: Checking: Claire: pink. In the description of the original question, at the start of the game, Claire has a pink ball. So Clare: pink is correct. Remaining:
                Comment 6: I have checked through all parts of the text and found no errors. So Thought 1 is correct. Yes"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Alice, Bob, and Claire are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Lola, Bob is dancing with Rodrigo, and Claire is dancing with Patrick.
                Throughout the song, the dancers often trade partners. First, Alice and Bob switch partners. Then, Claire and Bob switch partners. Finally, Bob and Alice switch partners. At the end of the dance, Alice is dancing with
                Options:
                (A) Lola
                (B) Rodrigo
                (C) Patrick
                Thought 1: At the start: Alice: Lola, Bob: Rodrigo, Claire: Patrick.
                Thought 2: Alice and Bob switch partners: Alice: Rodrigo, Bob: Lola, Claire: Patrick.
                Thought 3: Claire and Bob switch partners: Alice: Rodrigo, Bob: Patrick, Claire: Lola.
                Thought 4: Bob and Alice switch partners: Alice: Patrick, Bob: Rodrigo, Claire: Lola.
                Thought 5: At the end of the dance, Alice is dancing with Rodrigo. So the answer is (B)
                
                Is Thought 5 correct? Check through each part of the text and determine whether there are any errors."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 5 by checking through each part of the text. Remaining: At the end of the dance, Alice is dancing with Patrick. So the answer is (A)
                Comment 2: Checking: At the end of the dance. In Thought 4, Bob and Alice switch partners. According to the description in the original question, this is the final swap. Thought 5 is at the end of the dance, so At the end of the dance is correct. Remaining: Alice is dancing with Patrick. So the answer is (A)
                Comment 3: Checking: Alice is dancing with Rodrigo. In Thought 4, after the final swap, Alice's partner is Patrick. So Alice is dancing with Rodrigo is incorrect.
                Comment 4: Alice is dancing with Rodrigo is incorrect. So Thought 5 is incorrect. No"""
            ),
        },
    )
}

WORD_SORTING_PROMPTS = {
    "DIRECT_TEMPLATE" : (
        "Q: Sort the following words alphabetically: List: {input}\n{steps}\nIs"
        ' there a mistake in this sequence? Write "No" if there are no mistakes, or'
        " the number N if there is a mistake in Thought N."
    ),

    "DIRECT_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "For each sequence of steps, identify the first mistake made, if"
                " any."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Q: Sort the following words alphabetically: List: oven costume counterpart
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "oven": "o" (15). "costume": "c" (3). "counterpart": "c" (3).
                Thought 2: We now have: (3) ["costume" ? "counterpart"] < (15) "oven".
                Thought 3: Now let's sort this subpart ["costume" ? "counterpart"] by looking at their second letters. The second letter: "costume": "o" (15). "counterpart": "o" (15).
                Thought 4: We now have: (15) ["costume" ? "counterpart"] for the subpart. Hence, we have ["costume" ? "counterpart"] < "oven".
                Thought 5: Now let's sort this subpart ["costume" ? "counterpart"] by looking at their third letters. The third letter: "costume": "s" (19). "counterpart": "n" (14).
                Thought 6: We now have: (14) "counterpart" < (19) "costume" for the subpart. Hence, we have "counterpart" < "costume" < "oven".
                Thought 7: I have now sorted all the words. The answer is counterpart costume oven
                Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "5"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Q: Sort the following words alphabetically: List: newt arson parthia seismography mugho aspect census
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "newt": "n" (14). "arson": "a" (1). "parthia": "p" (16). "seismography": "s" (19). "mugho": "m" (13). "aspect": "a" (1). "census": "c" (3).
                Thought 2: We now have: (1) ["arson" ? "aspect"] < (3) "census" < (13) "mugho" < (14) "newt" < (16) "parthia" < (19) "seismography".
                Thought 3: Now let's sort this subpart ["arson" ? "aspect"] by looking at their second letters. The second letter: "arson": "r" (18). "aspect": "s" (19).
                Thought 4: We now have: (18) "arson" < (19) "aspect" for the subpart. Hence, we have "arson" < "aspect" < "census" < "mugho" < "newt" < "parthia" < "seismography".
                Thought 5: I have now sorted all the words. The answer is arson aspect census mugho newt parthia seismography
                Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Q: Sort the following words alphabetically: List: hypochlorite ponderosa phone credulity
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "hypochlorite": "h" (8). "ponderosa": "p" (16). "phone": "p" (16). "credulity": "c" (3). 
                Thought 2: We now have: (3) "credulity" < (8) "hypochlorite" < (16) ["ponderosa" ? "phone"].
                Thought 3: Now let's sort this subpart ["ponderosa" ? "phone"] by looking at their second letters. The second letter: "ponderosa": "o" (15). "phone": "h" (8).
                Thought 4: We now have: (8) "phone" < (15) "ponderosa" for the subpart. Hence, we have "credulity" < "phone" < "ponderosa".
                Thought 5: I have now sorted all the words. The answer is credulity phone ponderosa
                Is there a mistake in this sequence? Write "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {"role": "assistant", "content": "4"},
    ),

    "DIRECT_PERSTEP_TEMPLATE" : (
        "Task: Sort the following words alphabetically: List: {input}\n{steps}\nQ:"
        ' Is Thought {current_step} correct? Write "Yes" if it is correct, and "No"'
        " if it is not. Do not need to explain."
    ),

    "DIRECT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                ' solving the question. Write "Yes" if it is correct, and "No" if'
                " it is not."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: oven costume counterpart
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "oven": "o" (15). "costume": "c" (3). "counterpart": "c" (3).
                Q: Is Thought 1 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "Yes"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: hypochlorite ponderosa phone credulity
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "hypochlorite": "h" (8). "ponderosa": "p" (16). "phone": "p" (16). "credulity": "c" (3). 
                Thought 2: We now have: (8) "hypochlorite" < (16) ["ponderosa" ? "phone"] < (3) "credulity".
                Q: Is Thought 2 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "No"},
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: newt arson parthia seismography mugho aspect census
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "newt": "n" (14). "arson": "a" (1). "parthia": "p" (16). "seismography": "s" (19). "mugho": "m" (13). "aspect": "a" (1). "census": "c" (3).
                Thought 2: We now have: (1) ["arson" ? "aspect"] < (3) "census" < (13) "mugho" < (14) "newt" < (16) "parthia" < (19) "seismography".
                Thought 3: Now let's sort this subpart ["arson" ? "aspect"] by looking at their second letters. The second letter: "arson": "r" (18). "aspect": "s" (19).
                Thought 4: We now have: (18) "arson" < (19) "aspect" for the subpart. Hence, we have "arson" < "aspect" < "census" < "newt" < "parthia" < "seismography".
                Q: Is Thought 4 correct? Write "Yes" if it is correct, and "No" if it is not."""
            ),
        },
        {"role": "assistant", "content": "No"},
    ),

    "COT_TEMPLATE" : (
        "Task: Sort the following words alphabetically: List: {input}\n{steps}\nQ:"
        " Is there a mistake in this sequence? If so, where is the first mistake?"
        " Break down your thought process and show your reasoning step-by-step."
        ' Your answer should be "No" if there are no mistakes, or the number N if'
        " there is a mistake in Thought N."
    ),
    
    "COT_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "For each sequence of steps, identify the first mistake made, if"
                " any."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: oven costume counterpart
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "oven": "o" (15). "costume": "c" (3). "counterpart": "c" (3).
                Thought 2: We now have: (3) ["costume" ? "counterpart"] < (15) "oven".
                Thought 3: Now let's sort this subpart ["costume" ? "counterpart"] by looking at their second letters. The second letter: "costume": "o" (15). "counterpart": "o" (15).
                Thought 4: We now have: (15) ["costume" ? "counterpart"] for the subpart. Hence, we have ["costume" ? "counterpart"] < "oven".
                Thought 5: Now let's sort this subpart ["costume" ? "counterpart"] by looking at their third letters. The third letter: "costume": "s" (19). "counterpart": "n" (14).
                Thought 6: We now have: (14) "counterpart" < (19) "costume" for the subpart. Hence, we have "counterpart" < "costume" < "oven".
                Thought 7: I have now sorted all the words. The answer is counterpart costume oven
                Q: Is there a mistake in this sequence? If so, where is the first mistake? Break down your thought process and show your reasoning step-by-step. Your answer should be "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: This sequence of thoughts sorts words alphabetically by rearranging them by the first letter, then the second letter, etc. and keeping track of the sorted order. To find the first mistake, I need to check the correctness of each Thought one by one, starting with Thought 1.
                Comment 2: Thought 1 lists the first letter of "oven" ('o'), the first letter of "costume" ('c'), and the first letter of "counterpart" ('c'). It identifies their positions in the alphabet: 'o' is the 15th letter; 'c' is the 3rd letter. So Thought 1 is correct.
                Comment 3: Thought 2 rearranges the words according to the alphabet position of the first letter. There are two words starting with 'c', so we don't know which one comes first. The words from the original question, "oven", "costume", and "counterpart", are all included and sorted correctly. So Thought 2 is correct.
                Comment 4: The question asks to sort the words "oven", "costume", and "counterpart", but "costume" and "counterpart" both start with 'c'. Thought 3 lists the second letter of "costume" ('o') and the second letter of "counterpart" ('o'). It identifies their positions in the alphabet: 'o' is the 15th letter. So Thought 3 is correct.Comment 5: Thought 4 rearranges the words according to the alphabet position of the second letter. There are two words starting with 'co', so we don't know which one comes first. "oven" is included once and sorted correctly; "costume" is included once and sorted correctly; "counterpart" is included once and sorted correctly. So Thought 4 is correct.
                Comment 6: The question asks to sort the words "oven", "costume", and "counterpart", but "costume" and "counterpart" both start with 'co'. Thought 5 lists at the third letter of "costume" ('s'), and the fourth letter of "counterpart" ('u'). Thought 5 should look at the third letter of counterpart ('u'). So Thought 5 is incorrect.
                Comment 7: Thoughts 1 to 4 are correct, but Thought 5 is incorrect. So the answer is 5"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: hypochlorite ponderosa phone credulity
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "hypochlorite": "h" (8). "ponderosa": "p" (16). "phone": "p" (16). "credulity": "c" (3). 
                Thought 2: We now have: (3) "credulity" < (8) "hypochlorite" < (16) ["ponderosa" ? "phone"].
                Thought 3: Now let's sort this subpart ["ponderosa" ? "phone"] by looking at their second letters. The second letter: "ponderosa": "o" (15). "phone": "h" (8).
                Thought 4: We now have: (8) "phone" < (15) "ponderosa" for the subpart. Hence, we have "credulity" < "hypochlorite" < "phone" < "ponderosa".
                Thought 5: I have now sorted all the words. The answer is credulity hypochlorite phone ponderosa
                Q: Is there a mistake in this sequence? If so, where is the first mistake? Break down your thought process and show your reasoning step-by-step. Your answer should be "No" if there are no mistakes, or the number N if there is a mistake in Thought N."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: This sequence of thoughts sorts words alphabetically by rearranging them by the first letter, then the second letter, etc. and keeping track of the sorted order. To find the first mistake, I need to check the correctness of each Thought one by one, starting with Thought 1.
                Comment 2: Thought 1 lists the first letter of "hypochlorite" ('h'), the first letter of "ponderosa" ('p'), the first letter of "phone" ('p'), and the first letter of "credulity" ('c'). So Thought 1 is correct. It identifies their positions int he alphabet: 'h' is the 8th letter, 'c' is the 3rd letter, and 'p' is the 16th letter. So Thought 1 is correct.
                Comment 3: Thought 2 rearranges the words according to the alphabet position of the first letter. There are two words starting with 'p' so we don't know which one comes first. 'hypochlorite' is included once and sorted correctly; 'ponderosa' is included once and sorted correctly; 'phone' is included once and sorteed correctly; and 'credulity' is included once and sorted correctly. So Thought 2 is correct.
                Comment 4: The question asks to sort the words "hypochlorite", "ponderosa", "phone", and "credulity", but "ponderosa" and "phone" both start with 'p'. Thought 3 lists the second letter of "ponderosa" ('o') and the second letter of "phone" ('h'). It identifies their positions in the alphabet: 'o' is the 15th letter, and 'h' is the 8th letter. So Thought 3 is correct.
                Comment 5: Thought 4 rearranges the words ponderosa and phone according to the alphabet position of the second letter. "hypochlorite" is included once and sorted correctly; "ponderosa" is included once and sorted correctly; "phone" is included once and sorted correctly; and "credulity" is included once and sorted correctly. So Thought 4 is correct.
                Comment 6: Thought 5 is the final thought and provides the answer. According to Thought 4, the correct order is "credulity" < "hypochlorite" < "phone" < "ponderosa", so Thought 5 is correct. So the answer is No"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: newt arson parthia seismography mugho aspect census
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "newt": "n" (14). "arson": "a" (1). "parthia": "p" (16). "seismography": "s" (19). "mugho": "m" (13). "aspect": "a" (1). "census": "c" (3).
                Thought 2: We now have: (1) ["arson" ? "aspect"] < (3) "census" < (13) "newt" < (14) "newt" < (16) "parthia" < (19) "seismography".
                Thought 3: Now let's sort this subpart ["arson" ? "aspect"] by looking at their second letters. The second letter: "arson": "r" (18). "aspect": "s" (19).
                Thought 4: We now have: (18) "arson" < (19) "aspect" for the subpart. Hence, we have "arson" < "aspect" < "census" < "newt" < "newt" < "parthia" < "seismography".
                Thought 5: I have now sorted all the words. The answer is arson aspect census newt newt parthia seismography.
                Thought 6: Answer: arson aspect census newt parthia seismography
                Q: Is there a mistake in this sequence? If so, where is the first mistake? Break down your thought process and show your reasoning step-by-step. Your answer should be "No" if there are no mistakes, or the number N if the first mistake in Thought N."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: This sequence of thoughts sorts words alphabetically by rearranging them by the first letter, then the second letter, etc. and keeping track of the sorted order. To find the first mistake, I need to check the correctness of each Thought one by one, starting with Thought 1.
                Comment 2: Thought 1 lists the first letter of "newt" ('n'), the first letter of "arson" ('a'), the first letter of "parthia" ('p'), the first letter of "seismography" ('s'), the first letter of "mugho" ('m'), the first letter of "aspect" ('a'), and the first letter of "census" ('c'). It identifies their positions in the alphabet: 'n' is the 14th letter, 'a' is the 1st letter, 'p' is the 16th letter, 's' is the 19th letter, 'm' is the 13th letter, and 'c' is the 3rd letter. So Thought 1 is correct.
                Comment 3: Thought 2 rearranges the words according to the alphabet position of the first letter. There are two words starting with 'a', so we don't know which one comes first. "mugho" is not included; "newt" is included twice. So Thought 2 is incorrect.
                Comment 4: Thought 1 is correct, but Thought 2 is incorrect. So the answer is 2"""
            ),
        },
    ),

    "COT_PERSTEP_TEMPLATE" : (
        "Task: Sort the following words alphabetically: List: {input}\n{steps}\nQ:"
        " Is Thought {current_step} correct? Check through each word in the"
        " original list and determine whether they are correctly described."
    ),

    "COT_PERSTEP_MESSAGES" : (
        {
            "role": "user",
            "content": (
                "Identify whether a thought is correct and contributes towards"
                " solving the question. End your response with Yes if the"
                " thought is correct, No if the thought is incorrect."
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: oven costume counterpart
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "oven": "o" (15). "costume": "c" (3). "counterpart": "c" (3).
                Q: Is Thought 1 correct? Check through each word in the original list and determine whether they are correctly described."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 1 by checking each word in the list: oven costume counterpart. Remaining: oven costume counterpart
                Comment 2: Checking: oven. The first letter of "oven" is "o", which is the 15th letter of the alphabet. So "oven": "o" (15) is correct. Remaining: costume counterpart
                Comment 3: Checking: costume. The first letter of "costume" is "c", which is the 3rd letter of the alphabet. So "costume": "c" (3) is correct. Remaining: counterpart
                Comment 4: Checking: counterpart. The first letter of "counterpart" is "c", which is the 3rd letter of the alphabet. So "counterpart": "c" (3) is correct. Remaining:
                Comment 5: Thought 1 does not include any other words, and all words from the original list are included. So Thought 1 is correct. Yes"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: hypochlorite ponderosa phone credulity
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "hypochlorite": "h" (8). "ponderosa": "p" (16). "phone": "p" (16). "credulity": "c" (3). 
                Thought 2: We now have: (8) "hypochlorite" < (16) ["ponderosa" ? "phone"] < (3) "credulity".
                Q: Is Thought 2 correct? Check through each word in the original list and determine whether they are correctly described."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 2 by checking each word in the list: hypochlorite ponderosa phone credulity. Remaining: hypochlorite ponderosa phone credulity
                Comment 2: Checking: hypochlorite. hypochlorite is placed before ponderosa and phone because the first letter "h" (8) is before the first letter "p" (16). So (8) "hypochlorite" < (16) ["ponderosa" ? "phone"] is correct. Remaining: ponderosa phone credulity
                Comment 3: Checking: ponderosa. ponderosa is placed after hypochlorite because the first letter "p" (16) is after the first letter "h" (8) in the alphabet. ponderosa is placed in the same position as phone because the first letter "p" (16) is the same. ponderosa is placed before credulity, but the first letter "c" (3) is before the first letter "p" (16) in the alphabet. So (16) ["ponderosa" ? "phone"] < (3) "credulity" is incorrect.
                Comment 4: (16) ["ponderosa" ? "phone"] < (3) "credulity" is incorrect, so Thought 2 is incorrect. No"""
            ),
        },
        {
            "role": "user",
            "content": textwrap.dedent(
                """\
                Task: Sort the following words alphabetically: List: newt arson parthia seismography mugho aspect census
                Thought 1: I should start by looking at the first letter of the words in the list. The first letter: "newt": "n" (14). "arson": "a" (1). "parthia": "p" (16). "seismography": "s" (19). "mugho": "m" (13). "aspect": "a" (1). "census": "c" (3).
                Thought 2: We now have: (1) ["arson" ? "aspect"] < (3) "census" < (13) "mugho" < (14) "newt" < (16) "parthia" < (19) "seismography".
                Thought 3: Now let's sort this subpart ["arson" ? "aspect"] by looking at their second letters. The second letter: "arson": "r" (18). "aspect": "s" (19).
                Thought 4: We now have: (18) "arson" < (19) "aspect" for the subpart. Hence, we have "arson" < "aspect" < "census" < "newt" < "parthia" < "seismography".
                Q: Is Thought 4 correct? Check through each word in the original list and determine whether they are correctly described."""
            ),
        },
        {
            "role": "assistant",
            "content": textwrap.dedent(
                """\
                Comment 1: I will identify any mistakes in Thought 4 by checking each word in the list: newt arson parthia seismography mugho aspect census. Remaining: newt arson parthia seismography mugho aspect census
                Comment 2: Checking: newt. newt is placed after census because the first letter "n" (14) is after the first letter "c" (3). newt is placed before parthia because the first letter "n" (14) is before the first letter "p" (16). So "census" < "newt" < "parthia" is correct. Remaining: arson parthia seismography mugho aspect census
                Comment 3: Checking: arson. arson is placed before aspect because the first letter "a" (1) is the same and the second letter "r" (18) is before the second letter "s" (19). So "arson" < "aspect" is correct. Remaining: parthia seismography mugho aspect census
                Comment 4: Checking: parthia. parthia is placed after newt because the first letter "p" (16) is after the first letter "n" (14). parthia is placed before seismography because the first letter "p" (16) is before the first letter "s" (19). So "newt" < "parthia" < "seismography" is correct. Remaining: seismography mugho aspect census
                Comment 5: Checking: seismography. seismography is placed after parthia because the first letter "s" (19) is after the first letter "p" (16). So "parthia" < "seismography" is correct. Remaining: mugho aspect census
                Comment 6: Checking: mugho. mugho is missing from the list. So "arson" < "aspect" < "census" < "newt" < "parthia" < "seismography" is incorrect.
                Comment 7: "arson" < "aspect" < "census" < "newt" < "parthia" < "seismography" is incorrect, so Thought 4 is incorrect. No"""
            ),
        },
    )
}

class SelfCheck:
    def __init__(self):
        pass

    def initialize_record_list(self, data):
        """
        Initialize record list for SelfCheck.
        """
        record_list = []
        for entry in data:
            record = {
                "question": entry["input"],
                "formalized_question": self.formalize_question(entry["input"]),
                "steps": entry["steps"],
                "conditions": self.get_conditions(self.formalize_question(entry["input"])),
                "step_record": [{"status": "initialized", "original_step": step} for step in entry["steps"]]
            }
            record_list.append(record)
        return record_list

    def formalize_question(self, input_text):
        """
        Formalize question by adding "\s" to each sentence.
        """
        sentences = input_text.split(". ")
        return " ".join([f"\\s {sentence.strip()}" for sentence in sentences if sentence.strip()])

    def get_conditions(self, formalized_question):
        """
        Extract conditions from the formalized question.
        """
        return [cond.strip() for cond in formalized_question.split("\\s") if cond.strip()]

    def input_for_target_extraction(self, question, steps, i):
        """
        Generate input for extracting the target of a specific step.
        """
        string = 'The following is a part of the solution to the problem:\n\n'
        string += f"Problem: {question}\n\n"
        string += "\n\n".join(steps[:i+1])
        string += f'\n\nWhat specific action does the step "{steps[i]}" take? Please give a brief answer using a single sentence.'
        return string
    
    def input_for_information_collection(self, question, steps, i, conditions):
        """
        Generate input for collecting relevant information for a specific step.
        """
        string = f"This is a math question:\n\nQuestion: {question}\n\n"
        string += "The following is information extracted from the question:\n\n"
        for j, condition in enumerate(conditions):
            string += f"Information {j}: {condition}\n"

        if i >= 1:
            string += "\nThe following are previous steps in the solution:\n\n"
            for j in range(i):
                string += f"Thought {j}: {steps[j]}\n"

            string += f'\nWhich previous steps or information does the next step "{steps[i]}" directly follow from?'
        else:
            string += f'\nWhich information does the first reasoning step "{steps[i]}" directly follow from?'

        return string
    
    def input_for_rerunning(self, target, conditions, steps):
        """
        Generate input for regenerating a specific step.
        """
        string = 'We are solving a math problem with the following information:\n\n'
        for j, condition in enumerate(conditions):
            string += f"Information {j}: {condition}\n"
        string += "\n"

        for j, step in enumerate(steps):
            string += f"Previous step {j}: {step}\n"
        string += "\n"

        string += f'The target for the next step is:\n\n{target}\n\nPlease attempt to achieve the target using the provided information and previous steps.'
        return string
    
    def input_for_compare(self, original_step, regenerated_step):
        """
        Generate input for comparing the original and regenerated steps, ensuring concise output.
        """
        string = "The following are two solutions to a step in a math problem:\n\n"
        string += f"Solution 1: {regenerated_step}\n\n"
        string += f"Solution 2: {original_step}\n\n"
        string += (
            'Based on the two solutions, choose one of the following options:\n'
            '- "support": if Solution 1 supports the conclusion of Solution 2.\n'
            '- "contradict": if Solution 1 contradicts the conclusion of Solution 2.\n'
            '- "is not directly related to": if Solution 1 is unrelated to the conclusion of Solution 2.\n\n'
            "Your answer should be one of the three options above without any additional explanation."
        )
        return string

    def get_verification_result(self, comparison_output):
        """
        Interpret the comparison output for verification.
        """
        if "contradict" in comparison_output.lower():
            return -1
        elif "support" in comparison_output.lower():
            return 1
        return 0

    def verify_steps(self, record_list, model_call):
        """
        Verify steps one by one using the given model_call function.
        Returns the index of the first incorrect step or -1 if all are correct.
        """
        for record in record_list:
            question = record["question"]
            step_record = record["step_record"]

            for i, step_info in enumerate(step_record):
                if step_info["status"] == "initialized":
                    target_input = self.input_for_target_extraction(question, record["steps"], i)
                    step_info["target"] = model_call([{"role": "user", "content": target_input}])
                    step_info["status"] = "target_extracted"

                if step_info["status"] == "target_extracted":
                    info_input = self.input_for_information_collection(
                        question, record["steps"], i, record["conditions"]
                    )
                    step_info["conditions_used"] = model_call([{"role": "user", "content": info_input}]).split("\n")
                    step_info["status"] = "information_collected"

                if step_info["status"] == "information_collected":
                    rerun_input = self.input_for_rerunning(
                        step_info["target"], record["conditions"], record["steps"][:i]
                    )
                    step_info["regenerated_step"] = model_call([{"role": "user", "content": rerun_input}])
                    step_info["status"] = "rerun"

                if step_info["status"] == "rerun":
                    compare_input = self.input_for_compare(
                        step_info["original_step"],
                        step_info["regenerated_step"]
                    )
                    comparison_output = model_call([{"role": "user", "content": compare_input}])
                    step_info["verification_result"] = self.get_verification_result(comparison_output)
                    step_info["status"] = "finished"

                    if step_info["verification_result"] == -1:
                        return i

        # Return -1 if all steps are correct
        return -1