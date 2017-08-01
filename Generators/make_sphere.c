//
//  make_sphere.c
//  
//
//  Created by svarma on 11/4/16.
//
//

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include "my_header.h"
char path_defns_file[FILE_LEN], error_flag_file[FILE_LEN];
//#include "IO_coor.c"
//#include "path_querry.c"

#define LEN1 8
#define LEN2 256
#define DELTA 4.16
#define PI 3.142


int main(int argc, char *argv[])
{
    char out_coor_file[LEN2], ch;
    int ctr, i, j, k, maxi, midi;
    float x0, y0, z0, dist, shift, theta, phi, dtheta, dtheta0, dphi, curr_r;
    double x,y,z, box_size, radius;
    line *head, *l;
    FILE *fp;

    //Read input from command line
    sscanf(argv[1], "%s", out_coor_file);
    sscanf(argv[2], "%lf", &box_size);
    sscanf(argv[3], "%lf", &radius);

    //Make sphere
    
    dphi=2.0*atan(DELTA/(2.0*radius));
    printf("dphi = %f\n", dphi);
    
    ctr=0;
    head=(line *)malloc(sizeof(line));
    head->next=NULL;
    l=head;
    
    
    for(phi=0;phi<=PI;phi+=dphi)
    {
        curr_r = radius * cos(PI/2-phi);
        dtheta=2.0*asin(DELTA/(2.0*curr_r));
        printf("dtheta = %f\n", dtheta);
    
        for(theta=0;theta<=2*PI;theta+=dtheta)
            {
                l->next=(line *)malloc(sizeof(line));
                l=l->next;
                l->next=NULL;
                strcpy(l->res_type, "CH4");
                strcpy(l->atom_type, "CM");
                strcpy(l->name, "ATOM");
                l->atom_num = ctr;
                l->res_num = ctr++;
                l->x = radius * sin(phi) * sin(theta);
                l->y = radius * sin(phi) * cos(theta);
                l->z = radius * cos(phi);
            }
        
    }
    
    //print sphere
    fp=fopen(out_coor_file, "w+");
    fprintf(fp, "CRYST1  90.000  90.000  90.000  90.00  90.00  90.00 P 1\n");
    l=head->next;
    while(l)
        {
            l->x += box_size/2.0;
            l->y += box_size/2.0;
            l->z += box_size/2.0;
            fprintf(fp,"%-6s%5d %-3s %-4s %4d    %8.3f%8.3f%8.3f\n", l->name, l->atom_num, l->atom_type, l->res_type, l->res_num, l->x, l->y, l->z);
        
        l=l->next;
        }
    
    fclose(fp);
    
    
    
    
    
}
