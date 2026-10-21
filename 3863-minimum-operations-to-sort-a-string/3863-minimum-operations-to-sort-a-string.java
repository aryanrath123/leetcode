class Solution {
    public int minOperations(String s) {
        int n = s.length();
        char[] a = s.toCharArray();
        char[] b = a.clone();
        Arrays.sort(b);

        if (Arrays.equals(a, b)) return 0;
        if (n == 2) return -1;

        int min = 0, max = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] < a[min]) min = i;
            if (a[i] >= a[max]) max = i;
        }

        if (min == 0 || max == n - 1) return 1;
        if (min == n - 1 && max == 0) return 3;
        return 2;
    }
}