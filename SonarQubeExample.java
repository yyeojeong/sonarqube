public class SonarQubeExample {
    private int value;

    public SonarQubeExample(int initialValue) {
        this.value = initialValue;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int newValue) {
        this.value = newValue;
    }

    public int addNumbers(int a, int b) {
        return a + b;
    }

    public String convertToString(int number) {
        return Integer.toString(number);
    }

    public void printValue() {
        System.out.println("Current value: " + value);
    }

    public static void main(String[] args) {
        SonarQubeExample example = new SonarQubeExample(10);
        example.printValue();
        int result = example.addNumbers(5, 7);
        System.out.println("Result of addition: " + result);
        example.setValue(20);
        example.printValue();
    }
}