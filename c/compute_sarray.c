#include <stdio.h>
#include <stdlib.h>
#include "sarray.h"
 
int main(int argc, char * argv[])
{
   int ind, i,length;
   char *num, *infile = argv[1];
   char *outfile = argv[2];
   int *intarray;

   length = atoi(argv[3]);
   intarray = (int *) malloc((length+1)* sizeof(int));

   FILE *fp = fopen(infile, "r");

   for(ind =0; ind < length; ind++)
      fscanf(fp, "%d\n", &intarray[ind]);
   intarray[length] = 0;
     
   fclose(fp);
   /*for(i=0; i<length+1; i++)
      printf("%d\n", intarray[i]);
   printf("---");
   */

   ind = sarray(intarray, length+1);

   fp =fopen(outfile, "w");
   for(i=0; i<length+1; i++)
      fprintf(fp, "%d\n", intarray[i]);

   fclose(fp);
   free(intarray);
   return(0);
}

