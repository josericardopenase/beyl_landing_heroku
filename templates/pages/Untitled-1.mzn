
% Data file for simple production planning model
Products = { Tiempo, Dinero, Volumen, Peso };
profit = [400, 450]; % in cents
Resources = { Cepillo, Camiseta, PastaDientes, Pantalon, Cinturon, Movil, Ordenador, Camara, TecladoMecanico, Toalla, PatitoDeGoma, MojoPicon, PanDeSandwich, HandbookMinizinc};
capacity = [4000, 6, 2000, 500, 500];
consumption= [| 250, 2, 75, 100, 0,
| 200, 0, 150, 150, 75 |];

