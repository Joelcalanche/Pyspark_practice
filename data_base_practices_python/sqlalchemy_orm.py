


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy	 import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/household", echo=True)

Base = declarative_base()

class Project(Base):
	__tablename__ ="projects"
	__table_arg__ = {'schema':'household'}

	project_id = Column(Integer, primary_key=True)
	title = Column(String(length=50))
	description = Column(String(length=50))

def __repr__(self):
	return "<Project(title'{0}', description='1'>".format(self.title, self.description)



class Task(Base):
	__tablename__ = "tasks"
	__table_args__ = {'schema':'household'}

	task_id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey('household.projects.project_id'))
	description = Column(String(length=50))


	# nombre de la clase no de la tabla, esto es el complemento de la foreignkey e indica que hay una relacion entre modelos mas alla de tablas 
	project = relationship("Project")

	def __repr__(self):
	return "<Task(title'{0}', description='1'>".format(self.title, self.description)

# create las tablas

Base.metadata.create_all(engine)



session_maker = sessionmaker()

session_maker.configure(bind=engine)

session = session_maker()


organize_closet_project = Project(title='Organize closet', description='Organize closet')


session.add(organize_closet_project)

## we need commit

session.commit()

tasks = [Task(project_id=organize_closet_project.project_id, description='deasdsda')]

session.bulk_save_objects(tasks)

session.commit()


 our_project = sesion.query(Project).filter_by(title='Organize_closet').first()

 print(our_project)

 our_task = session.query(Task).all()
 print(our_task)