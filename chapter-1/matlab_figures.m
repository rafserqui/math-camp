close all
clear all
clc

xmin = -10;
xmax = -xmin;
ymin = 2*xmin;
ymax = -ymin;

npoints = 100;
lw = 1.2;
cmap =  [0    0.4470    0.7410
	    0.8500    0.3250    0.0980
	    0.9290    0.6940    0.1250
	    0.4940    0.1840    0.5560
	    0.4660    0.6740    0.1880
	    0.3010    0.7450    0.9330
	    0.6350    0.0780    0.1840];

    
%%% Different Lines
x = linspace(xmin,xmax,npoints);

f1 = 1-x;
f2 = 2.*x;
f3 = 8;
f4 = -4.*ones(size(x));

figure
plot(x,f1,'-','LineWidth',lw,'Color',cmap(1,:))
hold on
grid on
box off
plot(x,f2,'--','LineWidth',lw,'Color',cmap(2,:))
line([8 8],[ymin ymax],'LineStyle','-.','LineWidth',lw,'Color',cmap(3,:))
plot(x,f4,'.','LineWidth',lw,'Color',cmap(4,:))
legend({'$f(x) = 1-x$','$f(x) = 2x$','$x = 8$','$f(x) = -4$'},'location',...
    'northwest','Interpreter','latex')
ylim([ymin ymax])
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
xticklabel = get(gca,'XTickLabel');
set(gca,'XTickLabel',xticklabel,'FontName','Times','FontSize',11);
print(gcf,'Ch1_files\Ch1_2_0','-depsc','-r0')

%%% Differences in Slopes
slope = -2:0.5:1.5;

figure
hold on
grid on
for ll = 1:length(slope)
   lambda = slope(ll);
   tempy = lambda.*x;
   leg = ['$ \lambda = ',num2str(lambda)];
   pp(ll) = plot(x,tempy,'-','LineWidth',lw,'Color',cmap(ll,:),'DisplayNname',leg)
end
hold off
lgd = legend;
lgd.NumColumns = 2;