#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int charToIndex(char c) {
  return ((int) c) - 97;
}

int number_needed(char *a, char *b) {
  char charsA[26] = { 0 };
  char charsB[26] = { 0 };
  int lengthA = strlen(a);
  int lengthB = strlen(b);
  if (lengthA >= lengthB) {
    for (int i = 0; i < lengthB; i++) {
      charsA[charToIndex(a[i])]++;
      charsB[charToIndex(b[i])]++;
    }
    for (int i = lengthB; i < lengthA; i++) {
      charsA[charToIndex(a[i])]++;      
    }
  } else {
    for (int i = 0; i < lengthA; i++) {
      charsA[charToIndex(a[i])]++;
      charsB[charToIndex(b[i])]++;
    }
    for (int i = lengthA; i < lengthB; i++) {
      charsB[charToIndex(b[i])]++;      
    }
  } 
  int diff = 0;
  for (int i = 0; i < 26; i++) {
    diff += abs(charsA[i] - charsB[i]);
  }
  return diff;
}

int main() {
  char* a = (char *) malloc(512000 * sizeof(char));
  scanf("%s",a);
  char* b = (char *) malloc(512000 * sizeof(char));
  scanf("%s",b);

  printf("%d\n", number_needed(a, b));
  
  return 0;
}
