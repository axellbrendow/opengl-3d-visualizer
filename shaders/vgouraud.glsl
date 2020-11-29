attribute vec4 vPosition ;
attribute vec3 vNormal ;

uniform mat4 modelViewMatrix ;
uniform mat4 projectionMatrix ;
uniform mat3 normalMatrix ;

uniform vec4 ambientProduct ;
uniform vec4 diffuseProduct ;
uniform vec4 specularProduct ;
uniform float shininess ;
uniform vec4 lightPosition ;

void main ()
{
    vec4 eyePosition = modelViewMatrix * vPosition ;
    vec3 N = normalMatrix * vNormal ;
    vec3 L = lightPosition.xyz - eyePosition.xyz ;
    vec3 E = - eyePosition.xyz ;
    vec3 R = reflect (-E , N);

    N = normalize (N);
    L = normalize (L);
    E = normalize (E);

    float NdotL = dot (N , L);
    float Kd = max ( NdotL , 0.0) ;
    float Ks = ( NdotL < 0.0) ? 0.0 : pow ( max ( dot (R , E) , 0.0), shininess );

    vec4 diffuse = Kd * diffuseProduct ;
    vec4 specular = Ks * specularProduct ;
    vec4 ambient = ambientProduct ;

    gl_Position = projectionMatrix * eyePosition ;
    gl_FrontColor = ambient + diffuse + specular ;
    gl_FrontColor .a = 1.0;
}
