int N = 10;
int[] f = new int[N];

void setup() {
  size(400, 400);
  f[0]=0; f[1]=1;
  for (int i=2; i<N; i++){
    f[i] = f[i-1] + f[i-2];
  }
  noLoop();
}

void draw(){
  background(30);
  int x = 0;
  for (int i=0; i<N; i++){
    fill(200,100,50,200);
    rect(x, height - f[i]*10, f[i]*10, f[i]*10);
    x += f[i]*10;
  }
}
