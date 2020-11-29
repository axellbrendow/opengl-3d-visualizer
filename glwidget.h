#ifndef GLWIDGET_H
#define GLWIDGET_H

#include <iostream>
#include <fstream>
#include <limits>

#include <QtOpenGL>

#include "camera.h"
#include "light.h"
#include "material.h"
#include "trackball.h"

class GLWidget : public QGLWidget
{
    Q_OBJECT

public:
    explicit GLWidget(QWidget *parent = nullptr);
    virtual ~GLWidget();

protected:
    void initializeGL();
    void resizeGL(int width, int height);
    void paintGL();
    void mouseMoveEvent ( QMouseEvent * event );
    void mousePressEvent ( QMouseEvent * event );
    void mouseReleaseEvent ( QMouseEvent * event );
    void wheelEvent ( QWheelEvent * event );
    void keyPressEvent ( QKeyEvent * event );

private:
    bool bgBlack;
    unsigned int numVertices;
    unsigned int numFaces;
    QVector4D *vertices;
    QVector3D *normals;
    QVector2D *texCoords;
    QVector4D *tangents;
    unsigned int *indices;

    QGLBuffer * vboVertices ;
    QGLBuffer * vboNormals ;

    QGLBuffer * vboTexCoords ;
    QGLBuffer * vboTangents ;
    QGLBuffer * vboIndices ;

    QGLShader * vertexShader ;
    QGLShader * fragmentShader ;
    QGLShaderProgram * shaderProgram ;
    unsigned int currentShader ;

    int texID [2];

    QMatrix4x4 modelViewMatrix ;
    QMatrix4x4 projectionMatrix ;

    Camera camera ;
    Light light ;
    Material material ;

    TrackBall trackBall ;

    double zoom;
    int fpsCounter;

    QTimer timer;

    void readOFFFile(const QString &fileName);
    void genNormals();
    void genTexCoordsCylinder () ;
    void genTangents () ;
    void createVBOs () ;
    void destroyVBOs () ;
    void createShaders () ;
    void destroyShaders () ;

    QPointF pixelPosToViewPos ( const QPointF &p);

signals:
//    void takeScreenshot();
    void statusBarMessage(QString ns);

public slots:
    void toggleBackgroundColor();
    void showOpenFileDialog();
    void animate();
};

#endif // GLWIDGET_H
