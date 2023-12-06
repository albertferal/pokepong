# Proyecto CI-CD KeepCoding - Albert Fernández

#### En este proyecto implementamos un pipeline de CircleCI que use distintos recursos para una app hecha en PyGame.

## Estructura: 
#### Se divide en 3 directorios principales:
## .circleci
 - Directorio principal del pipeline. >> [Pipeline aquí](.circleci)

    -  Construye la app y ejecuta los tests necesarios (pytest, linting y code coverage).
    -  Se sincroniza con SonarCloud para hacer un analisis del código completo, para ello usamos su Orb.

    ![SonarCloud](Screenshots/sonarcloud1.jpg)
    
    ![SonarCloud](Screenshots/sonarcloud2.jpg)
    
    -  Se sincroniza con Snyk para hacer un analisis de vulnerabilidades del código.
    
    ![Snyk](Screenshots/snyk1.jpg)
    
    ![Snyk](Screenshots/snyk2.jpg)
    
    -  Terminamos generando nuestro artefacto en .zip y publicándolo directamente a Git.
    
    ![RepoArtifact](Screenshots/artifact-repo.jpg)
    
    -  Todo el Workflow es dependiente, no se puede ejecutar un trabajo hasta que termine el anterior.

    ![Pipeline](Screenshots/pipeline1.jpg)
    
    ![Pipeline](Screenshots/pipeline2.jpg)
    
    ![Pipeline](Screenshots/pipeline3.jpg)

## Game: 
- Directorio principal en el que se encuentra la app y todas sus dependencias y requerimientos. >> [App aquí](Game)
    -  Para correr le aplicación de Pokepong lo puedes hacer mediante VSC. (Play en main.py)

    ![App corriendo](Screenshots/app-pokepong.jpg)

    -  Tenemos el subdirectorio tests donde se crean las prubeas para pytest, linting, etc...

## k8s: 
- En este directorio tenemos los manifiestos yml para el despliegue de la app en Kubernetes. >> [Manifiestos aquí](k8s)
    - Consta de 3 sencillos archivos yml para poder lanzar la app a un cluster de Kubernetes.
    - Lo desplegamos en ArgoCD siguiendo la [documentación oficial](https://argo-cd.readthedocs.io/en/stable/cli_installation/).
    - Una vez dentro de la interfaz de ArgoCD, podemos hacer el despliegue manualmente o a través de un archivo .yml >> [ArgoCD yml aquí](pong-app.yml)

    ![Pipeline](Screenshots/argocd.jpg)

    ![Pipeline](Screenshots/argocd2.jpg)

    ![Pipeline](Screenshots/argocd3.jpg)

    Vídeo explicativo de la prráctica >> https://www.loom.com/share/793d1245e05f4d2c81911e2b7afd4a06