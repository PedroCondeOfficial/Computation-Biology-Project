#define LEN_CHAR 8
#define SEG_NAME 2
#define FILE_LEN 256
#define DIM_A 4096
#define DIM_B 256
#define EXEC_LEN 64
#define PI 3.142
#define CMD_LEN 256
#define MAX_GRIDS 5
#define MAX_EXT 5
#define CLUST_I 500
#define CLUST_J 50

#define CO_bond 1.36 /*in Angstroms*/ 
#define CN_bond 1.33
#define SS_bond 2.04
#define COdb_bond 1.23
#define error   0.05
#define H_bond 3.00
#define gas_constant 1.98586

static char atom_map[]            = "hydrogen_map.dat";
/*static char charge_rad_file[]     = "neutral.dat";*/
static char tech_specs_pka[]      = "tech_specs_pka.dat";
static char tech_specs_force_1d[] = "tech_specs_force_1d.dat";
static char tech_specs_pot_1d[]   = "tech_specs_pot_1d.dat";
static char deleted_atoms_file[]  = "deleted_atoms_file";


static char nullstr[]            = "\0";
static char cleanup[]            = "YES";
static char debug[]              = "OFF";

struct pdb_line{
  char name[LEN_CHAR];
  int atom_num;
  char atom_type[LEN_CHAR];
  char res_type[LEN_CHAR];
  int res_num;
  char seg_name[SEG_NAME];
  char icode[SEG_NAME];
  float x;
  float y;
  float z;
  float q;
  float r;
  struct pdb_line *next;
};
typedef struct pdb_line line; 


struct pdb_dline{   
  char name[LEN_CHAR];
  int atom_num;
  char atom_type[LEN_CHAR];
  char res_type[LEN_CHAR];
  int res_num;
  char seg_name[SEG_NAME];
  char icode[SEG_NAME];
  double x;
  double y;
  double z;
  double q;
  double r;
  struct pdb_dline *next;
};
typedef struct pdb_dline dline;


struct linked_float_type{
  float node;
  struct linked_float_type *next;
};
typedef struct linked_float_type lnkd_f;


struct linked_double_coor_type{
  double x;
  double y;
  double z;
  struct linked_double_coor_type *next;
};
typedef struct linked_double_coor_type lnkd_lf_coor;


struct linked_char_type{
  char node[LEN_CHAR];
  struct linked_char_type *next;
};
typedef struct linked_char_type lnkd_c;



struct linked_integer_type{
  int node;
  struct linked_integer_type *next;
};
typedef struct linked_integer_type lnkd_i;


struct linked_atom_database_type{
  char res[LEN_CHAR];
  int res_num;
  char atom[LEN_CHAR];
  float q;
  float epsi;
  float sigm;
  float r;
  struct linked_atom_database_type *next;
};
typedef struct linked_atom_database_type lnkd_atom_database;


struct charge_table_line{
  char res_type[LEN_CHAR];
  int res_num;
  float ch;
  struct charge_table_line *next;
};
typedef struct charge_table_line ct_line; 

struct pot_profile_line{
  char res_type[LEN_CHAR];
  int  res_num;
  char atom_type[LEN_CHAR];
  float x;
  float y;
  float z;
  float pot;
  struct pot_profile_line *next;
};
typedef struct pot_profile_line ppl; 


struct force_profile_line{
  char res_type[LEN_CHAR];
  int  res_num;
  char atom_type[LEN_CHAR];
  float  x,  y,  z;
  float fx, fy, fz;
  struct force_profile_line *next;
};
typedef struct force_profile_line fpl; 


void line_copy_ppl(ppl *a, ppl *b)
{ 
  strcpy(a->atom_type, b->atom_type);
  strcpy(a->res_type, b->res_type);
  a->res_num = b->res_num; 
  a->x = b->x;
  a->y = b->y;
  a->z = b->z;
  a->pot = b->pot;
} 


void swap_ppl(ppl *a, ppl *b)
{
  ppl *temp;
  
  temp=(ppl *)malloc(sizeof(ppl));
  temp->next = NULL;

  line_copy_ppl(temp, a); 

  line_copy_ppl(a, b);

  line_copy_ppl(b,temp);
}


void line_copy(line *a, line *b)
{
  strcpy(a->name,b->name);
  a->atom_num=b->atom_num;
  strcpy(a->atom_type,b->atom_type);
  strcpy(a->res_type,b->res_type);
  strcpy(a->seg_name,b->seg_name);
  strcpy(a->icode,b->icode);
  a->res_num=b->res_num;
  a->x=b->x;
  a->y=b->y;
  a->z=b->z;
  a->q=b->q;
  a->r=b->r;
}

void line_d2f(dline *a, line *b)
{
  strcpy(b->name,a->name);
  b->atom_num=a->atom_num;
  strcpy(b->atom_type,a->atom_type);
  strcpy(b->res_type,a->res_type);
  strcpy(b->seg_name,a->seg_name);
  strcpy(b->icode,a->icode);
  b->res_num=a->res_num;   
  b->x=(float)a->x;
  b->y=(float)a->y;  
  b->z=(float)a->z;  
  b->q=(float)a->q;
  b->r=(float)a->r;
}


void copy_atom_def(lnkd_atom_database *a, lnkd_atom_database *b)
{
  strcpy(a->res, b->res);
  strcpy(a->atom, b->atom);
  a->q = b->q; 
  a->r = b->r; 
  a->epsi = b->epsi; 
  a->sigm = b->sigm; 
}


      
