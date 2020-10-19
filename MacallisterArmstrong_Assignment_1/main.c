#include <stdio.h>
int problem_one();
int problem_two();
int problem_three();
int problem_four();
int problem_five();
int problem_six();

int main() {
    problem_one();
    problem_two();
    problem_three();
    problem_four();
    problem_five();
    problem_six();

    return 0;
}

int problem_one() {
    float f;
    f = 2.5;
    printf("%.10f\n", f);

    return 0;
}

int problem_two() {
    float f;
    f = -1.0/10.0;
    printf("%.10f\n", f);

    return 0;
}

int problem_three() {
    double d;
    d = 1/3;
    printf("%f\n", d);
    d = 1.0/3.0;
    printf("%f\n", d);

    return 0;
}

int problem_four() {
    double d;
    d = 9999999.3399999999;
    printf("%f\n", d);
    float f;
    f = (float) d;
    printf("%f\n", f);

    return 0;
}

int problem_five() {
    int i;
    i = 30000*30000;
    printf("%i\n", i);
    i = 40000*40000;
    printf("%i\n", i);
    i = 50000*50000;
    printf("%i\n", i);
    i = 60000*60000;
    printf("%i\n", i);
    i = 70000*70000;
    printf("%i\n", i);

    return 0;
}

int problem_six() {
    float f;
    f = 1e20;
    printf("%f\n", f);
    f = (1e20 + 3500000000);
    printf("%f\n", f);
    f = (1e20 + (3500000000 * 1000000000));
    printf("%f\n", f);
    float f2;
    f2 = 1e20;
    int i;
    for (i = 0; i < 1000000000; i++) {
        f2 += 3500000000;
    }
    printf("%f\n", f2);

    return 0;
}
