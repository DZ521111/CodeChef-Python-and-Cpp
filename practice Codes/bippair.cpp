// Author : Dhruv B Kakadiya


#include<bits/stdc++.h>
#define For(i,x,y) for (register int i=(x);i<=(y);i++)
#define FOR(i,x,y) for (register int i=(x);i<(y);i++)
#define Dow(i,x,y) for (register int i=(x);i>=(y);i--)
#define Debug(v) for (auto i:v) cout<<i<<" ";puts("")
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define ep emplace_back
#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define fil(a,b) memset((a),(b),sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pa;
typedef pair<ll,ll> PA;
typedef vector<int> poly;
inline ll read(){
    ll x=0,f=1;char c=getchar();
    while ((c<'0'||c>'9')&&(c!='-')) c=getchar();
    if (c=='-') f=-1,c=getchar();
    while (c>='0'&&c<='9') x=x*10+c-'0',c=getchar();
    return x*f;
}

inline void GG(){
	puts("YOU ARE IN TROUBLE");
	exit(0);
}

const int N = 110, K = 1110, M = 1e4+10, mod = 998244353;
int n,m,x[M],y[M],z[M],w[M],id[N];

inline int power(int a,int b){
	int ret=1;
	for (;b;b>>=1,a=1ll*a*a%mod) if (b&1) ret=1ll*ret*a%mod;
	return ret;
}
inline int Mod(int x){
	return x>=mod?x-mod:x;
}

int cnt[2],flag[N];
vector<int>e[N];
inline void dfs(int u,int k){
	flag[u]=k,cnt[k]++;
	for (auto v:e[u]) if (flag[v]==-1) dfs(v,k^1);
}

int a[N][N];
inline int Det(int a[N][N],int n){
	int ret=1;
	For(i,1,n){
		if (!a[i][i])
			For(j,i+1,n) if (a[j][i]){
				swap(a[i],a[j]),ret=mod-ret;
				break;
			}
		ret=1ll*ret*a[i][i]%mod;
		int inv=power(a[i][i],mod-2);
		For(j,i+1,n){
			int tmp=1ll*a[j][i]*inv%mod;
			For(k,i,n) a[j][k]=(a[j][k]+1ll*(mod-tmp)*a[i][k])%mod;
		}
	}
	return ret;
}

int ret[K],pos[K];
inline void DFT(int *a,int n){
	FOR(i,0,n) pos[i]=(pos[i>>1]>>1)|((i&1)<<9);
	FOR(i,0,n) if (i<pos[i]) swap(a[i],a[pos[i]]);
	for (int i=1;i<n;i<<=1){
		int wn=power(3,(mod-1)/2/i);
		for (int j=0;j<n;j+=i<<1)
			for (int k=0,w=1;k<i;k++,w=1ll*w*wn%mod){
				int x=a[j+k],y=1ll*w*a[i+j+k]%mod;
				a[j+k]=Mod(x+y),a[i+j+k]=Mod(x+mod-y);
			}
	}
}
inline void IDFT(int *ret,int n){
	DFT(ret,n),reverse(ret+1,ret+n);
	int inv=power(n,mod-2);
	FOR(i,0,n) ret[i]=1ll*ret[i]*inv%mod;
}

int main(){
	srand(19260817);
	n=read(),m=read();
	For(i,1,m){
		x[i]=read()+1,y[i]=read()+1,z[i]=read(),w[i]=rand();
		e[x[i]].pb(y[i]),e[y[i]].pb(x[i]);
	}
	fil(flag,-1);
	For(i,1,n) if (flag[i]==-1){
		cnt[0]=cnt[1]=0,dfs(i,0);
		if (cnt[0]!=cnt[1]) GG();
	}
	For(i,1,m) if (flag[x[i]]>flag[y[i]]) swap(x[i],y[i]);
	cnt[0]=n/2,cnt[1]=n/2;
	Dow(i,n,1) id[i]=cnt[flag[i]]--;
//	printf("%d %d %d %d %d\n",id[1],id[2],id[3],id[4],id[5]);
	int g=power(3,(mod-1)/1024),tmp=1;
	For(i,0,1023){
		vector<int>pw(21);
		pw[0]=1;
		For(j,1,20) pw[j]=1ll*pw[j-1]*tmp%mod;
		For(j,1,n/2) For(k,1,n/2) a[j][k]=0;
		For(j,1,m) a[id[x[j]]][id[y[j]]]=1ll*pw[z[j]]*w[j]%mod;
		ret[i]=Det(a,n/2);
		tmp=1ll*tmp*g%mod;
	}
	IDFT(ret,1024);
	poly ans;
	For(i,0,1023) if (ret[i]) ans.pb(i);
	if (ans.empty()) GG();
	printf("%d\n",siz(ans));
	for (auto i:ans) printf("%d ",i);
}