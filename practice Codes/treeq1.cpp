// Author : Dhruv B Kakadiya


#include<bits/stdc++.h>
using namespace std;

typedef long long lint;
typedef long double louble;

template<typename T1,typename T2> inline T1 max(T1 a,T2 b){return a<b?b:a;}
template<typename T1,typename T2> inline T1 min(T1 a,T2 b){return a<b?a:b;}

const char lf = '\n';

namespace ae86
{
	const int bufl = 1<<15;

	char buf[bufl],*s=buf,*t=buf;

	inline int fetch()
	{
		if(s==t){t=(s=buf)+fread(buf,1,bufl,stdin);if(s==t)return EOF;}
		return *s++;
	}

	inline int ty()
	{
		int a=0,b=1,c=fetch();
		while(!isdigit(c))b^=c=='-',c=fetch();
		while(isdigit(c))a=a*10+c-48,c=fetch();
		return b?a:-a;
	}
}
using ae86::ty;

const int _ = 100007;

vector<pair<int,int>> e[_];
inline void adde(int a,int b){e[a].emplace_back(b,0);}
inline void addde(int a,int b){adde(a,b),adde(b,a);}

struct tla
{
#define lb(a) ((a)&(-(a)))

	int n;lint v[_],vv[_];

	tla(int _n=_-1){n=_n;for(int i=0;i<=n;i++)v[i]=vv[i]=0;}

	inline void add(int x,lint d,lint dd){while(x<=n)v[x]+=d,vv[x]+=dd,x+=lb(x);}
	inline lint sum(int x)
	{
		int a=x;lint d=0,dd=0;
		while(a>0)d+=v[a],dd+=vv[a],a-=lb(a);
		return d*(x+1)+dd;
	}

	inline void addlr(int l,int r,lint d){add(l,d,-d*l),add(r+1,-d,d*(r+1));}
	inline lint sumlr(int l,int r){if(l>r)return 0;return sum(r)-sum(l-1);}
	
#undef lb
};

int n,qn,fa[_]={0},sz[_]={0},dfn[_]={0},ndf[_]={0},dcnt=0;
lint val[_]={0};

void dfs(int x,int ff)
{
	fa[x]=ff,sz[x]=1,dfn[x]=++dcnt;
	for(int i=1,ii=e[x].size();i<ii;i++)
	{
		if(e[x][i].first==ff)swap(e[x][i],e[x][0]);
		int b=e[x][i].first;
		if(b)dfs(b,x),sz[x]+=sz[b];
	}
	ndf[x]=dcnt;
}

bool ban[_]={0};
int siz[_]={0};

void dfssiz(int x,int ff)
{
	siz[x]=1;
	for(auto i:e[x])
	{
		int b=i.first;
		if(!ban[b] && b!=ff && b)dfssiz(b,x),siz[x]+=siz[b];
	}
}

int geralt(int x,int ff,int allsiz)
{
	for(auto i:e[x])
	{
		int b=i.first;
		if(!ban[b] && b!=ff && b && siz[b]>allsiz/2)
			return geralt(b,x,allsiz);
	}
	return x;
}

int makegeralt(int x)
{
	dfssiz(x,-1),x=geralt(x,-1,siz[x]),ban[x]=1;
	for(auto &i:e[x])
	{
		int b=i.first;
		if(b && !ban[b])
			i.second=makegeralt(b);
	}
	return x;
}

tla t;

inline lint sumst(int x){return t.sumlr(dfn[x],ndf[x]);}

inline int bounding(int x,lint tar)
{
	int l=1,r=e[x].size()-1,ans=-1;
	while(r>=l)
	{
		int mid=(l+r)>>1,b=e[x][mid].first;
		lint temp=t.sumlr(dfn[x]+1,ndf[b]);
		if(tar<temp+temp)ans=mid,r=mid-1;
		else l=mid+1;
	}
	return ans;
}

int skyfucker(int x,lint allval)
{
	if(allval==0)return 0;
	int ans=0;
	ban[x]=1;
	if(sumst(x)<=allval/2)ans=skyfucker(e[x][0].second,allval);
	else
	{
		int b=bounding(x,allval);
		if(b<0)ans=x;
		else
		{
			int c=e[x][b].first;
			if(sumst(c)<=allval/2)ans=x;
			else ans=skyfucker(e[x][b].second,allval);
		}
	}
	ban[x]=0;
	return ans;
}

int findano(int x,lint allval)
{
	if(sumst(x)*2==allval)return e[x][0].first;
	int b=bounding(x,allval);
	if(b<0 && e[x].size()<=1)return x;
	b=max(b,1);int c=e[x][b].first;
	if(sumst(c)*2==allval)return c;
	if(b!=1 && sumst(e[x][1].first)*2==allval)return e[x][1].first;
	return x;
}

int rt;

int main()
{
	ios::sync_with_stdio(0),cout.tie(nullptr);

	n=ty(),qn=ty();
	for(int i=1;i<=n;i++)val[i]=ty();
	for(int i=1,a,b;i<n;i++)a=ty(),b=ty(),addde(a,b);
	adde(1,0);

	t=tla(n),dfs(1,0),rt=makegeralt(1);
	for(int i=1;i<=n;i++)t.addlr(dfn[i],dfn[i],val[i]);
	lint allval=t.sumlr(1,n);
	
	for(int qq=1;qq<=qn;qq++)
	{
		int op=ty(),a=ty(),b=ty();
		if(op==1)t.addlr(dfn[a],dfn[a],b),allval+=b;
		if(op==2)t.addlr(dfn[a],ndf[a],b),allval+=1ll*b*sz[a];
		int ans=skyfucker(rt,allval);
		cout<<min(ans,findano(ans,allval))<<lf;
	}
	
	return 0;
}
