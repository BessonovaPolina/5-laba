#Постройте иерархию классов в соответствии с вариантом задания:
#Вариант 3: Организация, страховая компания, нефтегазовая компания, завод. Журнал, книга, печатное издание, учебник. 

class Organization:
    def __init__(self, name):
        self.name = name

class Company(Organization):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

class InsuranceCompany(Company):
    pass

class OilAndGasCompany(Company):
    pass

class ManufacturingCompany(Company):
    pass

class PrintedMaterial(Company):
    pass

class Publication:
    def __init__(self, title):
        self.title = title

class Magazine(Publication):
    pass

class Book(Publication):
    pass
    
class EducationalMaterial(Publication):
    pass

organization = Organization("Google")
company = Company("Apple", "Техника")
insurance_company = InsuranceCompany("Росгосстрах", "Страхование")
oil_and_gas_company = OilAndGasCompany("Лукойл", "Нефтегазовая")
manufacturing_company = ManufacturingCompany("Toyota", "Машины")
publication = Publication("Статья")
magazine = Magazine("Time")
book = Book("Гарри поттер")
printed_material = PrintedMaterial("учебник", "Python большая книга примеров")

print(f"Организация: {organization.name}")
print(f"Компания: {company.name} ({company.type})")
print(f"Страховая компания: {insurance_company.name} ({insurance_company.type})")
print(f"Росгосстрах: ({insurance_company.type})")
print(f"нефтегазовая компания: {oil_and_gas_company.name} ({oil_and_gas_company.type})")
print(f"Компания-производитель: {manufacturing_company.name} ({manufacturing_company.type})")
print(f"Публикация: {publication.title}")
print(f"Журнал: {magazine.title}")
print(f"Книга: {book.title}")
print(f"Печатный материал: {printed_material.name} ({printed_material.type})")

