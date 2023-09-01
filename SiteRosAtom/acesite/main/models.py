from django.db import models

class fill_TODO(models.Model):

    uid = models.CharField('Код', max_length=50)
    utask = models.TextField('Задача')
    uname = models.CharField('Исполнитель', max_length=100)


    def __str__(self):
        return f"{self.uid} {self.utask} {self.uname}"
    
class System(models.Model):

    uCodeIS = models.CharField('Код ИС', max_length=100)
    uFullName = models.TextField('Полное наименование')
    uOrgCode = models.CharField('Код Организации', max_length=100)


    def __str__(self):
        return f"{self.uCodeIS} {self.uFullName} {self.uOrgCode}"
    

class Modules(models.Model):
    uShortName = models.CharField('Короткое название', max_length=100)
    uLongName = models.TextField('Полное название')
    uSystem = models.CharField('Система', max_length=100)
    uCodePackage = models.CharField('Код Package', max_length=100)
    uModulesID = models.CharField('id', max_length=50)
    uConstruction = models.CharField('Construction', max_length=100)
    uStage = models.CharField('Stage', max_length=100)

    def __str__(self):
        return f"{self.uShortName} {self.uLongName} {self.uSystem} {self.uCodePackage} {self.uModulesID} {self.uConstruction} {self.uStage}"
    
    
    
class Products(models.Model):
    uID = models.CharField('Код', max_length=50)
    uType = models.CharField('Type', max_length=100)
    uComponentA = models.CharField('Component A', max_length=100)
    uComponentB = models.CharField('Component B', max_length=100)
    uLinkedProducts = models.CharField('LinkedProducts', max_length=100)
    uName = models.TextField('Название')
    uStatus = models.CharField('Статус', max_length=100)
    uComand = models.CharField('Команда', max_length=100)
    uRP = models.CharField('РП', max_length=100)
    uStartTime = models.DateField('Дата начала', null=True, blank=True)
    uStopTime = models.DateField('Дата окончания', null=True, blank=True)
    uCustomer = models.CharField('Заказчик', max_length=100)
    uNotes = models.TextField('Notes')
    uDocumentation = models.URLField('Документация')
    uConstruction = models.CharField('Construction', max_length=100)
    uAncestor = models.CharField('Предок', max_length=50)
    uLinkProject = models.URLField('LinkProject')

    def __str__(self):
        return (
        f"{self.uID} {self.uType} {self.uComponentA} {self.uComponentB} \
        {self.uLinkedProducts} {self.uName} {self.uStatus} {self.uComand} \
        {self.uRP} {self.uStartTime} {self.uStopTime} {self.uCustomer} \
        {self.uNotes} {self.uDocumentation} {self.uConstruction} \
        {self.uAncestor} {self.uLinkProject}"
    )


class ArchLayout(models.Model):
    uArchID = models.CharField('Код', max_length=50)
    uSys_A = models.CharField('sys_A', max_length=100)
    uArchLink = models.CharField('link', max_length=100)
    uSys_B = models.CharField('sys_B', max_length=100)

    def __str__(self):
        return(f"{self.uArchID} {self.uSys_A} {self.uArchLink} {self.uSys_B} ")
    
class ProductsVeh(models.Model):
    uVehID = models.CharField('ID', max_length=50)
    uVehDate = models.DateField('Date', null=True, blank=True)
    uVehProductID = models.CharField('ProductID', max_length=50)
    uVehType = models.CharField('Type', max_length=100)
    uVehDescription = models.TextField('Description')
    uVehBaseDoc = models.TextField('Документ основания')
    uVehSubmDoc = models.TextField('Подтверждающий документ')
    uVehPriority = models.CharField('Priority', max_length=100)
    uVehClosed = models.BooleanField('Closed')

    def __str__(self):
        return(
            f"{self.uVehID} {self.uVehDate} {self.uVehProductID} {self.uVehType} \
               {self.uVehDescription} {self.uVehBaseDoc} {self.uVehSubmDoc} \
               {self.uVehPriority} {self.uVehClosed}"
            )
    
class ProductsVnedr(models.Model):
    uVnedrID = models.CharField('Код', max_length=50)
    uVnedrComponentA = models.CharField('ComponentA', max_length=100)
    uVnedrComponentB = models.CharField('ComponentB', max_length=100)
    uVnedrLinkedProducts = models.CharField('LinkedProducts', max_length=100)
    uVnedrName = models.TextField('Название')
    uVnedrStatus = models.CharField('Статус', max_length=100)
    uVnedrComand = models.CharField('Команда', max_length=100)
    uVnedrRP = models.CharField('РП', max_length=100)
    uVnedrStartTime = models.DateField('Дата начала', null=True, blank=True)
    uVnedrStopTime = models.DateField('Окончание', null=True, blank=True)
    uVnedrCustomer = models.CharField('Заказчик', max_length=100)
    uVnedrNotes = models.TextField('Notes')
    uVnedrDocumentation = models.URLField('Документация')
    uVnedrPlantUML = models.CharField('PlantUML', max_length=300)
    uVnedr_Status = models.CharField('_статус', max_length=100)
    uVnedrConstruction = models.CharField('Construction', max_length=100)
    uVnedrAncestor = models.CharField('Предшественник', max_length=50)
    uVnedrLinkProject = models.URLField('LinkProject')

    def __str__(self):
        return(
            f"{self.uVnedrID} {self.uVnedrComponentA} {self.uVnedrComponentB} {self.uVnedrLinkedProducts} \
                {self.uVnedrName} {self.uVnedrStatus} {self.uVnedrComand} {self.uVnedrRP} \
                    {self.uVnedrStartTime} {self.uVnedrStopTime} {self.uVnedrCustomer} {self.uVnedrNotes} \
                        {self.uVnedrDocumentation} {self.uVnedrPlantUML} {self.uVnedr_Status} {self.uVnedrConstruction} \
                            {self.uVnedrAncestor} {self.uVnedrLinkProject}"
        )

class Resources(models.Model):
    uResID = models.CharField('Код', max_length=50)
    uResName = models.CharField('ФИО', max_length=100)
    uResRole = models.CharField('Роль в проекте', max_length=100)
    uResLeader = models.BooleanField('Лидер')
    uResComand = models.CharField('Команда', max_length=200)
    uResCheck = models.CharField('Статус', max_length=100)
    uResReport = models.CharField('Репорт', max_length=100)

    
    def __str__(self):
        return(
            f"{self.uResID} {self.uResName} {self.uResRole} {self.uResLeader} {self.uResComand} {self.uResCheck} {self.uResReport}")



class ReportCommentsNew(models.Model):

    uProductIDReport = models.CharField('ID Продукта', max_length=50)
    uVehIDReport = models.CharField('ID Вехи', max_length=50)

    date = models.DateTimeField('Дата',auto_now_add=True)
    
    text = models.TextField('Комментарий')

    class Meta:
        ordering = ['-date']

    @property
    def last_comment(self):
        return self.comments.first()
            
    @property
    def last_comment_date(self):
        last = self.last_comment
        return last.date if last else None

    @property
    def last_comment_text(self):
        last = self.last_comment
        return last.text if last else None

    def __str__(self):
        return(f"{self.uProductIDReport} {self.uVehIDReport} {self.date} {self.text}")
    

# class ReportCommentNew(models.Model):

#     uProductIDReport = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments', verbose_name='Продукт')
#     uVehIDReport = models.ForeignKey(ProductsVeh, on_delete=models.CASCADE, related_name='comments', verbose_name='Веха')

#     date = models.DateTimeField('Дата',auto_now_add=True)
    
#     text = models.TextField('Комментарий')

#     class Meta:
#         ordering = ['-date']

#     @property
#     def last_comment(self):
#         return self.comments.first()
            
#     @property
#     def last_comment_date(self):
#         last = self.last_comment
#         return last.date if last else None


#     def __str__(self):
#         return(f"{self.uProductIDReport} {self.uVehIDReport} {self.date} {self.text}")
    

class ReportComments(models.Model):
    uProductIDReport = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments', verbose_name='Продукт')
    uVehIDReport = models.ForeignKey(ProductsVeh, on_delete=models.CASCADE, related_name='comments', verbose_name='Веха')

    date = models.DateTimeField('Дата',auto_now_add=True)
    
    text = models.TextField('Комментарий')

    class Meta:
        ordering = ['-date']

    @property
    def last_comment(self):
        return self.comments.first()
            
    @property
    def last_comment_date(self):
        last = self.last_comment
        return last.date if last else None


    def __str__(self):
        return(f"{self.uProductIDReport} {self.uVehIDReport} {self.date} {self.text}")
    