def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def test_function_name():
    """Test for function_name"""
    # Arrange
    setup
    # Act
    result = function_call
    # Assert
    assert result == expected_value