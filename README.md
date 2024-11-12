Omdat ik een sterke affiniteit heb met wolkenkrabbers en hun indrukwekkende architectuur, besloot ik een project te maken waarin ik deze interesse combineer met mijn passie voor programmeren. Dit project gebruikt objectgeoriënteerd programmeren (OOP) in Python om een aantal beroemde wolkenkrabbers te modelleren. Het doel was niet alleen om de eigenschappen van deze iconische gebouwen vast te leggen, maar ook om mijn kennis van OOP-technieken in Python verder te verdiepen.

Projectbeschrijving
In dit project heb ik een klasse genaamd Skyscraper gemaakt, waarmee je verschillende wolkenkrabbers kunt aanmaken en hun eigenschappen kunt vergelijken. Je kunt bijvoorbeeld de hoogte van verschillende gebouwen optellen, controleren of twee wolkenkrabbers hetzelfde type hebben, en zien welk gebouw hoger is.

OOP-technieken in dit project
Tijdens het ontwikkelen van dit project heb ik verschillende OOP-elementen toegepast en versterkt:

Encapsulation:
De attributen zoals name, bouwtype, gewicht, hoogte, en stad worden beschermd en beheerd via de methoden van de klasse.
Inheritance (Overerving):
Hoewel er in dit project geen directe overerving wordt gebruikt, biedt de structuur van de klasse de mogelijkheid om in de toekomst extra klassen af te leiden voor specifieke typen gebouwen.
Polymorphism (Polymorfisme):
De __str__ en __repr__ methoden zijn overschreven om een duidelijke en unieke stringweergave van elk object te geven.
Magic Methods (Dunder Methods):
Ik heb gebruikgemaakt van verschillende magic methods:
__eq__: Vergelijkt twee wolkenkrabbers op basis van hun naam en bouwtype.
__lt__: Vergelijkt de hoogte van twee wolkenkrabbers.
__add__: Tel de hoogte van twee wolkenkrabbers bij elkaar op.
__len__: Retourneert de hoogte van de wolkenkrabber als de lengte van het object.# Skycraper
